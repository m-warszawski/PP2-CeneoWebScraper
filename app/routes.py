from app import app
from flask import render_template, redirect, url_for, request, send_file
import json
import os
import requests
import markdown
from app.models.product import Product

@app.route('/')
def index():
    path = "./README.md"
    description = ''
    if os.path.exists(path):
        with open(path,'r', encoding="utf-8") as f:
            text = f.read()
            description = markdown.markdown(text, extensions=['tables'])
    return render_template("index.html.jinja", description=description)

@app.route('/extract', methods=["POST", "GET"])
def extract():
    if request.method == "POST":
        product_id = request.form.get("product_id")
        product = Product(product_id)
        product.extract_name()
        if product.product_name:
            product.extract_opinions().calculate_stats().draw_charts()
            product.export_opinions()
            product.export_product()
        else:
            error = "Ups... coś poszło nie tak"
            return render_template("extract.html.jinja", error=error)
        return redirect(url_for('product', product_id=product_id))
    else:
        return render_template("extract.html.jinja")

@app.route('/products')
def products():
    products = [filename.split(".")[0] for filename in os.listdir("app/opinions")]
    products_list = []
    for product_id in products:
        product = Product(product_id)
        product.import_product()
        stats = product.stats_to_file()
        products_list.append(stats)
    return render_template("products.html.jinja", products_list=products_list)

@app.route('/author')
def author():
    return render_template("author.html.jinja")

@app.route('/product/<product_id>')
def product(product_id):
    product = Product(product_id)
    product.import_product()
    stats = product.stats_to_dict()
    opinions = product.opinions_to_dict()
    return render_template("product.html.jinja", product_id=product_id, stats=stats, opinions=opinions)

@app.route('/plots/<product_id>')
def plots(product_id):
    return render_template("plots.html.jinja", product_id=product_id)

@app.route('/download/<product_id>', methods=['GET', 'POST'])
def download(product_id):
    path = "opinions/"+product_id+'.json'
    return send_file(path, as_attachment=True)