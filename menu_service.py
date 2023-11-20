from typing import Any

from bs4 import BeautifulSoup
import requests
import re

from schemas import FoodResponse


class MenuService():

    def __init__(self):
        pass

    def get_menu(self):

        menu = []

        url = "https://www.stw-ma.de/Essen+_+Trinken/Speisepl%C3%A4ne/Mensaria+Metropol.html"

        r = requests.get(url)

        data = r.text

        soup = BeautifulSoup(data, features="html.parser")
        table = soup.find('table', attrs={'class': 'speiseplan-table'})
        rows = table.find_all('tr:not(.wahlmenu)')
        text_regex = re.compile('[^a-zA-Z]')
        price_regex = re.compile('[^0-9,]')

        for row in rows:            
            headline = row.find(
                "td", attrs={'class': "speiseplan-table-menu-headline"})

            headline_text = headline.text.strip()
            # print("headline", headline.text.strip())
            name = row.find(
                "td", attrs={'class': "speiseplan-table-menu-content"})

            sups = name.find_all("sup")

            for sup in sups:
                sup.decompose()

            name_text: str = name.text.strip().replace(" ,", ",")

            # print("content", f"<{name_text}>")

            price = row.find(
                "i", attrs={'class': "price"})

            price_text = price_regex.sub("", price.text).replace(",", ".")

            # print("price", price.text)

            menu.append(FoodResponse(name=name_text,
                        category=headline_text, price=float(price_text)))
        return menu
