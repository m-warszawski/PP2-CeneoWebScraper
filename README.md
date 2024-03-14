# Ceneo Web Scraper

#### The structure of opinions on the website [Ceneo.pl](https://www.ceneo.pl/)
|Opinion component|Selector|Variable name|Data type|
|---------------|--------|--------------|----------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id|string|
|autor opinii|span.user-post__author-name|author|string|
|rekomendacja autora|span.user-post__author-recomendation > em|recommendation|string|
|liczba gwiazdek|span.user-post__score-count|stars|string|
|treść opinii|div.user-post__text|content|string|
|lista zalet|div\[class$=positives\] ~ div.review-feature__item|pros|lista|
|lista wad|div\[class$=negatives\] ~ div.review-feature__item|cons|lista|
|dla ilu osób przydatna|button.vote-yes > span|useful|string|
|dla ilu osób nieprzydatna|button.vote-no > span|useless|string|
|data wystawienia opinii|span.user-post__published > time:nth-child(1)\["datetime"\]|published|string|
|data zakupu produktu|span.user-post__published > time:nth-child(2)\["datetime"\]|purchased|string|

## Tech Stack
+ **Flask**	- a web application framework is classified as a micro-framework because it does not require specific tools or libraries
+ **JSON**	-	library for working with JSON data; it is part of the standard Python toolkit modules
+ **OS**	-	a library providing functions for interacting with the operating system; OS is part of the standard Python toolkit modules
+ **Requests**	-	a library for HTTP communication, for web scraping purposes and for communication with HTTP-based APIs
+ **Pandas**	-	a library for data manipulation and analysis; in particular, it offers data structures and operations for manipulating numerical tables and time series
+ **NumPy**     -    library adding support for large, multi-dimensional tables and arrays
+ **BeautifulSoup**	-	library for parsing HTML and XML documents. Creates a parsing tree for analysed pages that can be used to extract data from HTML, which is useful for + web scraping
+ **Matplotlib**	-	a graphing library for the Python programming language and its numerical extension NumPy
+ **Markdown**  -    a library for converting content between Markdown and HTML

## Screenshots
