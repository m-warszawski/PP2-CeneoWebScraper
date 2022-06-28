# Ceneo Web Scraper

- - -

#### Struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)
|Składowa opinii|Selektor|Nazwa zmiennej|Typ danych|
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

- - -

#### Zastosowane biblioteki
+ **Flask**	-	framework aplikacji webowych,j est sklasyfikowany jako micro-framework, ponieważ nie wymaga określonych narzędzi ani bibliotek
+ **JSON**	-	biblioteka służąca do pracy z danymi JSON;  wchodzi w skład standardowych modułów narzędziowych Pythona
+ **OS**	-	biblioteka udostępniająca funkcje do interakcji z systemem operacyjnym; OS wchodzi w skład standardowych modułów narzędziowych Pythona
+ **Requests**	-	biblioteka do komunikacji HTTP, do celów web scrapingu oraz komunikacji z API opartym o HTTP
+ **Pandas**	-	biblioteka do manipulacji i analizy danych; w szczególności oferuje struktury danych i operacje służące do manipulowania tabelami liczbowymi i szeregami czasowymi. 
+ **NumPy**     -   biblioteka dodająca obsługę dużych, wielowymiarowych tabel i macierzy
+ **BeautifulSoup**	-	biblioteka do analizowania dokumentów HTML i XML. Tworzy drzewo parsowania dla przeanalizowanych stron, które można wykorzystać do wyodrębnienia danych z HTML, co jest przydatne do + skrobania stron internetowych
+ **Matplotlib**	-	biblioteka do tworzenia wykresów dla języka programowania Python i jego rozszerzenia numerycznego NumPy
+ **Markdown**  -    biblioteka służąca do konwersji treści pomiędzy Markdown a HTML

- - -

#### Etapy pracy
##### -> Projekt strukturalny
1. Pobranie elementów pojedynczej opinii do niezależnych zmiennych
2. Zapisanie wszystkich elemntów pojedynczej opinii do jednej zmiennej \(słownik\)
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i dodnie ich do listy
4. Pobranie wszystkich opinii o produkcie z wszystkich stron i zapisanie ich do pliku .json
5. Dodanie możliowści podania id produktu przez użytkownika za pomocą klawiatury
6. Refaktoryzacja \(optymalizacja\) kodu:
    1. utworzenie funkcji do pobierania składowych strony HTML
    2. utworzenie słownika opisującego strukturę opinii wraz z selektorami poszczególnych elementów
    3. zamiana instrukcji pobierających składowe opinii do pojedynczych zmiennych i tworzących z nich słownik na wyrażenie słownikowe \(dictionary comprehension\) tworzące słownik reprezentujący pojedynczą opinię na podstawie słownika selektorów
7. Analiza opinii o wybranym produkcie
    1. wczytanie wszystkich opinii o wskazanym produkcie do obiektu DataFrame
    2. wyliczenie podstawowych statystyk na podstawie opinii
        1. liczba wszystkich opinii o produkcie
        2. liczba opinii w których autor podał listę zalet produktu
        3. liczba opinii w których autor podał listę wad produktu
        4. średnia ocena produktu
    3. przygotowanie wykresów na podstawie zawartości opinii
        1. udział poszczególnych rekomendacji w ogólnej liczbie opinii
        2. histogram częstości występowania poszczególnych ocen (liczby gwiazdek)
##### -> Projekt obiektowy
1. Utworzenie projektu we Flask'u, prosty routing
2. Utworzenie szblonów stron w Jinja
3. Rozbudowanie routingu o kod pobierający opinie
4. Routing oraz szablony dla strony produktu i listy produktów
5. Dodanie modeli Opinion i Product
    + utworznie niezbędnych metod
    + przeniesienie fragmentów kodu z routingu
    + plik utils
    + plik parameters
6. Poprawki w kodzie
    + nazwy zmiennych
    + obsługa błędów
    + modyfikacje metod
7. Stworzenie wyglądu za pomocą Bootstrapa
    + dodanie tabeli z opiniami
    + strona dla wykresów
    + buttony na stronie

- - -
