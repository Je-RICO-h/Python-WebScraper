import requests
import webbrowser
import random
import sys
from bs4 import BeautifulSoup


def scraping():
    try:
        url = "https://www.newsinlevels.com/"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
        site = requests.get(url=url, headers=headers).text

        soup = BeautifulSoup(site, "lxml")

        f = open("links.txt", "w+")
        f.write("")
        f.close()
        f = open("links.txt", "a+")
        print("Please wait...This process may take up minutes!")
        print("If you want to interupt it, press: CTRL + C")

        for news in soup.find_all("div", class_="news-block"):
            f.write(f"{news.a['href']}\n")

        for num in range(2, 261):
            url = "https://www.newsinlevels.com/"
            url = f"{url}page/{num}/"
            site = requests.get(url=url, headers=headers).text
            soup = BeautifulSoup(site, "lxml")
            for news in soup.find_all("div", class_="news-block"):
                f.write(f"{news.a['href']}\n")
        f.close()
        print("Scraping finished!\n")
        return
    except KeyboardInterrupt:
        print("Scraping interrupted by user!")
        return

def getlink():
    f = open("links.txt","r")
    link = random.choice(f.read().splitlines())
    try:
        webbrowser.open(link,new=2,autoraise=True)
    except webbrowser.Error():
        print("Could not open file: Browser Error!")

def main():
        print("Choose an option:")
        print("  1.Scrape news!")
        print("  2.Get a random news!")
        print("  3.exit")
        n = input("Option: ")
        print("\n")
        if n == "1":
            scraping()
        elif n == "2":
            getlink()
        else:
            sys.exit()
        main()

if __name__ == "__main__":
    main()