# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sched, time
from datetime import date, datetime

def buscar_btc_google_dolar(link_url):
    now = datetime.now()
    date_now = now.date()
    current_time = now.strftime("%H:%M:%S")
    url = link_url
    my_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"}

    try:
        page = requests.get(url, headers=my_headers)
        soup = BeautifulSoup(page.content , 'html.parser')
        btc_now = soup.find("span", attrs={'class': 'DFlfde SwHCTb'}).text
        print(f"{date_now} {current_time} 1BTC = ${btc_now}")

    except Exception as e:
        print('error ----> ', e)

url = "https://www.google.com/search?q=btc+now&gl=us&hl=en&pws=0&source=hp&ei=UhJqYcnEDZrQ1sQPsdKg6AY&iflsig=ALs-wAMAAAAAYWogYtuXhmQfz13qscH_Eu23zHzbIj7H&ved=0ahUKEwjJtbywzM3zAhUaqJUCHTEpCG0Q4dUDCAk&uact=5&oq=btc+now&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEMQCEEYQggIyBQgAEIAEMgUIABCABDIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgUILhCABDoLCC4QgAQQxwEQ0QM6CwguEIAEEMcBEKMCOggILhCABBCTAjoHCAAQgAQQClCkB1j4EWCiE2gAcAB4AIABc4gBgAaSAQMwLjeYAQCgAQE&sclient=gws-wiz"
buscar_btc_google_dolar(url)