import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/trending-cryptocurrencies/   "

response = requests.get(url)

if response.status_code != 200:
    print("Error: Failed to retrieve website content")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

top30_list = soup.find("ul", class_="sc-beb003d5-3 cJrmgS cmc-table")

if top30_list is None:
    print("Error: Failed to find top 30 list")
    exit()

products = []
for product in top30_list.find_all('li'):
    products.append(product.text.strip())

if 'old_products' not in locals():
    old_products = []


def send_notification():
    print("A new product has appeared!")


if set(products) != set(old_products):
    send_notification()

old_products = products


