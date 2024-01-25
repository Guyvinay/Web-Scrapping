import requests
from bs4 import BeautifulSoup
import json
import gzip
def scrapping_amazon_laptops(pincode):
    url = f'https://www.amazon.in/s?k=laptop'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    # Make the HTTP request
    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.content, "html.parser")

    links = soup.find_all("a",attrs={"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})

    link = links[3].get('href')
    product_url = 'https://amazon.in/'+link

    new_webpage = requests.get(product_url, headers=headers)

    new_soup = BeautifulSoup(new_webpage.content, "html.parser")


    title = new_soup.find('span', attrs={"id":"productTitle"}).text.strip()
    price = new_soup.find('span', attrs={"class":"a-price-whole"}).text
    rating = new_soup.find('span', attrs={"class":"a-icon-alt"}).text

    print(title) 
    print(price)
    print(rating)

scrapping_amazon_laptops(560001)    