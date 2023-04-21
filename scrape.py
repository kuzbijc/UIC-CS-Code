#pulling info from internet

from bs4 import BeautifulSoup
import urllib3

def scrape():
    manager=urllib3.PoolManager()
    website="https://www.math.uic.edu" 
    site=manager.request('GET',website)
    B=BeautifulSoup(site.data.decode('utf-8'),'lxml')
    #print(B.prettify())
    events=B.find('div',attrs={'class':'column events'})
    #print(events)
    sections=events.find_all('div',attrs={'class':'section'})
    for event in sections:
        #print(event)
        seminar=event.find('a').string
        speaker=event.find('span').string
        title=event.find('span',attrs={'style':'font-style: italic;'}).string
        print(speaker,seminar,title)
    
def main():
    scrape()

main()
