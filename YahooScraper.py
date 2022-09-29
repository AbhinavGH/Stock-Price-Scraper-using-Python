import bs4
import requests
from bs4 import BeautifulSoup
def parsePrice():
    r=requests.get ('https://finance.yahoo.com/quote/META?p=META')
    soup=bs4.BeautifulSoup(r.text, "xml")
    price=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px) W(100%) '})[0].find('fin-streamer').text
    return price
while True:
    print ('the current price: '+str (parsePrice()))