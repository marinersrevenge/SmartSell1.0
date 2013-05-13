CODE:
Rhydolabz.py
import re
import urllib2
from bs4 import BeautifulSoup


url=urllib2.urlopen("http://www.rhydolabz.com/index.php?main_page=index&cPath=152_123")
soup=BeautifulSoup(url,"xml")
productnames=[]
productName = soup.find_all(attrs = 'itemTitle')
for p in productName:
    productnames=p.contents[0].next
    print productnames
productprices=[]
productPrice=soup.find_all("strong")
for p in productPrice:
    productprices=p.get_text()
    print productprices
------------------------------------------------------------------------------------------------------------------
Simplelabs.py

import re
import urllib2
from bs4 import BeautifulSoup

for u in ("http://www.simplelabs.co.in/catalog/arduino-boards?page=1","http://www.simplelabs.co.in/catalog/arduino-boards","http://www.simplelabs.co.in/catalog/arduino-shields","http://www.simplelabs.co.in/catalog/arduino-shields?page=1","http://www.simplelabs.co.in/catalog/starter-kits","http://www.simplelabs.co.in/catalog/starter-kits?page=1"):
    
    url=urllib2.urlopen(u)

    soup=BeautifulSoup(url)
    name=soup.find_all(alt=True)
    vari=[]
    for n in name:
        vari=n
        pari=vari['alt']
        print pari

    price=soup.find_all("span",{"class":"uc-price"})

    vari1=[]
    for p in price:
        vari1=p.get_text()
        print vari1
 -----------------------------------------------------------------------------------------------------------------   
mgsuperlabs.py

import re
import urllib2
from bs4 import BeautifulSoup




url=urllib2.urlopen("http://mgsuperlabs.co.in/estore/index.php?route=product/category&path=20&limit=25")
soup=BeautifulSoup(url,"xml")


price=[]
for prices in soup.find_all("div",{"class":"price"}):
    price=prices.string
    print price

changed_price=[]
for newprice in soup.find_all("span",{"class":"price-new"}):
    changed_price=newprice.string
    print "and the changed part's price is:%s"%(changed_price)

name=[]

for names in soup.find_all("div",{"class":"name"}):
    name=names.string
    print name
------------------------------------------------------------------------------------------------------------------
explorelabs.py

import re
import urllib2
from bs4 import BeautifulSoup

url=urllib2.urlopen("http://store.explorelabs.com/index.php?main_page=products_all")
soup=BeautifulSoup(url,"xml")
data=soup.find_all("td",{"colspan":"2"})
Price=[]
fag=[]
gag=[]
for d in data:
    fag=d.strong
    for f in fag:
        gag=f.string
        print gag

for priceli in data:
  Price=priceli.find_all(text=re.compile("Price:"))
  print Price

------------------------------------------------------------------------------------------------------------------
ninecircuits.py

import urllib2
import re
from bs4 import BeautifulSoup

url=urllib2.urlopen("http://9circuits.com/store/products/?items_per_page=all")
soup=BeautifulSoup(url)
Sumresult=soup.findAll( attrs="pricedisplay")
Sumresult=soup.findAll("strong")



print "The names of the products are:"
for s in Sumresult:
    nameli=[]
    nameli.append(s.string)
    print nameli
print "The prices of products are:"
pprice=soup.findAll(attrs="pricedisplay")
for p in pprice:
    priceli=[]
    priceli.append(p.string)
    print priceli
  			
------------------------------------------------------------------------------------------------------------------
