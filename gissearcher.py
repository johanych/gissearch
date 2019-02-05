import requests
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

def get_urls(site, inurl):
       query = 'site:{0}+inurl:{1}'.format(site, inurl)
       for num in range(0,400,100):
           pag = num
           url = 'https://www.google.com/search?q={0}&filter=0&num=100&ie=utf-8&oe=utf-8&start=%s' % pag
           url2 = url.format(query)
           time.sleep(60)
           response = requests.get(url2, headers=headers)
           soup = BeautifulSoup(response.content, 'html.parser')
           tags = soup.find_all('div', class_='r')
           for tag in tags:
               print(tag.a['href'])
#               print(tag.a['href'].split('/')[3])

if __name__ == '__main__':
       get_urls("servicio.gis.com", "/rest/")
