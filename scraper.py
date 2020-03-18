#import bibliotek
import requests
from bs4 import BeautifulSoup
#adres URL przykładowej strony z opiniami
url = "https://www.ceneo.pl/91184998#tab=reviews_scroll"

#pobranie kodu HTML strony z podanego URL
page_response = requests.get(url)
page_tree = BeautifulSoup(page_response.text, 'html.parser')

#wydobycie z kodu HTML strony fragmentów odpowiadających poszczególnym opiniom
opinions = page_tree.find_all("li", "review-box")

#wydobycie składowych dla pojedynczej opinii
for opinion in opinions:
    opinion_id = opinion["data-entry-id"]
    author = opinion.find("div", "reviewer-name-line").string
    try:
        recomendation = opinion.find("div", "product-review-summary").find("em").string
    except AttributeError:
        recomendation = None

    stars = opinion.find("span", "review-score-count")
    try:
        purchased = opinion.find("div", "product-review-pz")
    except AttributeError:
        purchased = None

    dates = opinion.find("span", "review-time").find_all("time")
    review_date = dates.pop(0)["datetime"]
    try:
        purchase_date = dates.pop(0)["datetime"]
    except AttributeError:
        purchase_date = None

    useful = opinion.find("button", "vote-yes").find("span").string
    useless = opinion.find("button", "vote-no").find("span").string
    content = opinion.find("p", "product-review-body").get_text()

    try:
        pros = opinion.find("div", "pros-cell").find("ul").get_text()
    except AttributeError:
        pros = None

    try:
        cons = opinion.find("div", "cons-cell").find("ul").get_text()
    except AttributeError:
        cons = None

    #print(opinion_id, author, recomendation, useful, useless, content, stars, purchased)
    print(opinion_id, recomendation, stars, content, author, pros, cons, useful, useless, purchased, purchase_date, review_date)