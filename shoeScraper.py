from bs4 import BeautifulSoup as bSoup
from urllib.request import urlopen as req
import json
import os
import csv


class Scraper:



    def scrape(arr):
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

            arr[product_name] = currPrice

            '''
            print("brand: " + brand)
            print("product_name: " + product_name)
            print("shipping: " + shipping)
            print("price: " + "$" + currPrice)
            print("\n")
            '''

            f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "," + currPrice + "\n")

        f.close()
        return arr

#Scraper.scrape()

def determinePriceReduce(productName):
    path = 'C:\\Users\\anson\\Web_Scraper2\\product.csv'
    currArr = {}
    pathExists = os.path.exists(path)
    if (pathExists):
        with open(path, 'r') as currInfo:
            csv_reader = csv.reader(currInfo, delimiter= ",")
            count = 0
            for row in csv_reader:
                if (count != 0):
                    currArr[row[1]] = row[3]
                count += 1
    newArr = {}
    newArr = Scraper.scrape(newArr)
    if (newArr[productName] == None):
        return false
    if (pathExists):
        return float(newArr[productName]) < float(currArr[productName])
    return false


product = input("Enter a product as mentioned on the website: ")

print(determinePriceReduce(product))
