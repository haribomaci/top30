import os
import requests
from bs4 import BeautifulSoup
import time

# Function to scrape the website and extract the top 30 cryptocurrencies
def get_top_30():
    url = "https://coinmarketcap.com/trending-cryptocurrencies/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="cmc-table")
    rows = table.tbody.find_all("tr")
    top_30 = []
    # for row in rows[-3:]:
    for row in rows[:30]:
        name = row.find("p", class_="kKpPOn")
        if name is None:
            continue
        name = name.text.strip()
        price = row.find("span", class_="")
        if price is None:
            continue
        price = price.text.strip()
        print(name)
        top_30.append((name))
    return top_30

# Function to send a message to a Telegram bot
def send_message(new_crypto):
    print(f"új:{new_crypto}")
    token = "YOUR_TELEGRAM_BOT_TOKEN"
    chat_id = "YOUR_TELEGRAM_CHAT_ID"
    message = f"New cryptocurrency entered the top 30 list: {new_crypto}"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

# Main function to periodically scrape the website and check for new cryptocurrencies
def main():
    top_30 = get_top_30()
    print(top_30)
    while True:
        new_top_30 = get_top_30()
        print(new_top_30)
        for crypto in new_top_30:
            if crypto not in top_30:
                print(crypto,)
                send_message(f"New cryptocurrency entered the top 30 list: {crypto}")
        top_30 = new_top_30
        time.sleep(60) # wait for 60 seconds before making the next request

if __name__ == '__main__':
    main()
