from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time


def typePrint(text, delay=.05):
    for letter in text:
        print(letter, end='')
        time.sleep(delay)
    print("\n")


def get_content_string(url):
    list_of_links = []
    page = requests.get(url)
    page_soup = BeautifulSoup(page.content, 'html.parser')

    news = page_soup.find_all('h2', class_='article__title-main')
    for container in news:
        for link in container:
            list_of_links.append(str(link))
    for link in list_of_links:
        print(link[9:-4])


print("Welcome to the Skate news aggregator!"
      "\nShortly you will receive all recent news links from Transworld to stay up to date on the skate community!")
print()

name = input("What's your name? ")
print()
time.sleep(2)
print(f"Welcome, {name}! Let me get those articles for you!")
time.sleep(2)
typePrint("Retrieving article URLs...")
time.sleep(2)
print()
get_content_string("https://skateboarding.transworld.net/news/")
