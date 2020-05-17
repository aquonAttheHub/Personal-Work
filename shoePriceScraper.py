from bs4 import BeautifulSoup as bSoup
from urllib.request import urlopen as req
import json

url = "https://www.newegg.com/p/pl?N=100164064%204025%20600377499%20600213647%20600213652"

urlData = req(url)
pageHTML = urlData.read()
urlData.close()

#HTML parser
parsed = bSoup(pageHTML, "html.parser")

#QGrabs each product item from the 'Shoes' page of newegg.com.
containers = parsed.findAll('div', attrs={"class": "item-info"})

fileName = "product.csv"
f = open(fileName, "w")
headers = "brand, product_name, shipping, price\n"
f.write(headers)

for container in containers:
    brand = "NA"
    if (container.div.a != None):
        brand = container.div.a.img['title']
    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text
    getItemAction = container.findAll("div", {"class": "item-action"})[0]
    getCurrPrice = getItemAction.ul.findAll("li", {"class", "price-current"})
    currPrice = getCurrPrice[0].strong.text + getCurrPrice[0].sup.text
    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)
    print("price: " + "$" + currPrice)
    print("\n")

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "," + currPrice + "\n")

f.close()
