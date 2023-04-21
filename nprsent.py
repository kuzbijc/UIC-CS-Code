from bs4 import BeautifulSoup
import urllib3

def get_art_text(art_url):
    manager=urllib3.PoolManager()
    site=manager.request('GET',art_url)
    B=BeautifulSoup(site.data.decode('utf-8'),'lxml')
    Btmp=B.find('div',{'id':'storytext'})
    t=Btmp.get_text()
    return t

def scrapeNPR():
    manager=urllib3.PoolManager()
    npr_url="https://www.npr.org/sections/news/"
    site=manager.request('GET',npr_url)
    B=BeautifulSoup(site.data.decode('utf-8'),'lxml')
    #print(B.prettify())
    articles=B.find_all('h2',attrs={'class':'title'})
    for article in articles:
        title=article.find('a').string
        art_url=article.find('a')['href']
        print(get_art_text(art_url))
    
def main():
    scrapeNPR()

main()
