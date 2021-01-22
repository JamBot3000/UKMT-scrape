import requests
from bs4 import BeautifulSoup as BSHTML
import os
import json
import itertools

url_list = [
    "https://www.ukmt.org.uk/competitions/solo/intermediate-mathematical-challenge/archive/",
    "https://www.ukmt.org.uk/competitions/solo/junior-mathematical-challenge/archive/",
    "https://www.ukmt.org.uk/competitions/solo/senior-mathematical-challenge/archive/",
]

data = {}

for url in url_list:
    rating = url[42].upper() + "MC"
    data[rating] = {}

    for year in range(2004, 2019):
        try:
            content = requests.get(url + str(year)).content
            soup = BSHTML(content, features="html.parser")
        except:
            pass

        images = soup.findAll("img")
        images = [image["src"] for image in images]
        images = [
            "https://ukmt.org.uk" + image
            for image in images
            if "individual-problems" in image
        ]

        questions = dict(itertools.zip_longest(*[iter(images)] * 2, fillvalue=""))
        data[rating][str(year)] = {"questions": questions}

with open("file.json", "w") as file:
    json.dump(data, file)