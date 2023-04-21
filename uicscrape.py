from bs4 import BeautifulSoup
import urllib3

def get_article(url):
    manager=urllib3.PoolManager()
    site=manager.request('GET',url)
    B=BeautifulSoup(site.data.decode('utf-8'),'lxml')
    
def scrapeBBC():
    manager=urllib3.PoolManager()
    website="https://today.uic.edu/uicnews/section/uic-news/"
    site=manager.request('GET',website)
    B=BeautifulSoup(site.data.decode('utf-8'),'lxml')
    #print(B.prettify())
    events=B.find_all('div',attrs={'class':'news-release-info clearfix'})
    #print(events)
    for event in events:
        title=event.find('a').string
        print(title)
        event_url=event.find('a')['href']
        print(event_url)
        article=get_article(event_url)
        print("----------------------------------")

def sent_analysis(article):
    pos=0
    neg=0
    ntrl=0
    p=set()
    n=set()
    stop=set()

    with open('positive.txt','r') as f:
        for line in f:
            word=line.replace('/n','')
            p.add(word)
    with open('negative.txt','r') as f:
        for line in f:
            word=line.replace('/n','')
            n.add(word)
    with open('stop.txt','r') as f:
        for line in f:
            word=line.replace('/n','')
            stop.add(word)

    art=article.lower()
    art=art.replace('.','')
    art=art.replace(',','')
    art=art.replace('!','')
    art=art.replace('?','')
    A=set(art.split(' '))
    B=set([word for word in A if word not in stop])
    pos=len(B.intersection(p))
    neg=len(B.intersection(n))
    print("positive sentiment (in %):" , 100*(pos/len(B)))
    print("negative sentiment (in %):" , 100*(neg/len(B)))
        
def main():
    scrapeBBC()
    
main()
