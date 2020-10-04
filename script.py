#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as BSHTML
import os

'''
Note this is extremely bad
Also this specific script will download both images **and** answers so I should fix that later
'''

os.system('mkdir MATHS-IMAGES')
os.system('mkdir MATHS-IMAGES/intermediate;mkdir MATHS-IMAGES/junior;mkdir MATHS-IMAGES/senior')

def get_images(search_url, rating):
    base_url = 'https://www.ukmt.org.uk'
    search_url = search_url

    for year in range(2004, 2019):
        os.system(f'mkdir MATHS-IMAGES/{rating}/{str(year)}; mkdir MATHS-IMAGES/{rating}/{str(year)}/questions;mkdir MATHS-IMAGES/{rating}/{str(year)}/answers')

    question_array = []
    answer_array = []

    for year in range(2004, 2019):

        question = True

        try:
            r = requests.get(f'{search_url}{str(year)}')
            soup = BSHTML(r.content, features="lxml")
            images = soup.findAll('img')
            for image in images:
                if 'individual-problems' in image.decode() and question == True:
                    question_array.append(base_url + image['src'])
                    question = False
                else:
                    answer_array.append(base_url + image['src'])
                    question = True
        except:
            pass

    num = 1
    for question in question_array:
        year = '20' + question.split("/")[-2][-2:]
        print(f'getting question {str(num)}/{str(len(question_array))}')
        os.system(f'wget {question} -q -P MATHS-IMAGES/{rating}/{year}/questions/')
        num += 1

    num = 1
    for answer in answer_array:
        year = '20' + answer.split("/")[-2][-2:]
        print(f'getting answer {str(num)}/{str(len(answer_array))}')
        os.system(f'wget {answer} -q -P MATHS-IMAGES/{rating}/{year}/answers/')
        num += 1

search_links = [
    'https://www.ukmt.org.uk/competitions/solo/intermediate-mathematical-challenge/archive/',
    'https://www.ukmt.org.uk/competitions/solo/junior-mathematical-challenge/archive/',
    'https://www.ukmt.org.uk/competitions/solo/senior-mathematical-challenge/archive/'
]
get_images(search_links[0], 'intermediate')
get_images(search_links[1], 'junior')
get_images(search_links[2], 'senior')