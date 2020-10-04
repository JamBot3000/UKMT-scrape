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
    image_array = []
    for i in range(2004, 2019):
        os.system(f'mkdir MATHS-IMAGES/{rating}/{str(i)}')
        try:
	        r = requests.get(f'{search_url}{str(i)}')    
        except:
            pass
        soup = BSHTML(r.content)
        images = soup.findAll('img')
        for image in images:
            if 'individual-problems' in image.decode():
                image_array.append(base_url + image['src'])

        array_length = len(image_array)
        num = 1
    for i in image_array:
        year = '20' + i.split("/")[-2][-2:]
        print(f'getting image {str(num)}/{str(array_length)}')
        os.system(f'wget {i} -q -P MATHS-IMAGES/{rating}/{year}')
        num += 1

search_links = [
    'https://www.ukmt.org.uk/competitions/solo/intermediate-mathematical-challenge/archive/',
    'https://www.ukmt.org.uk/competitions/solo/junior-mathematical-challenge/archive/',
    'https://www.ukmt.org.uk/competitions/solo/senior-mathematical-challenge/archive/'
]
get_images(search_links[0], 'intermediate')
get_images(search_links[1], 'junior')
get_images(search_links[2], 'senior')