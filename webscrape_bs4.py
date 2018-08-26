#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:05:33 2018

@author: clayton
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&IsNodeId=1&N=100167523%20600361769'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
    try:
        brand = container.div.div.a.img["title"]
    except:
        brand = "empty"
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_containter = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_containter[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + "," + product_name.replace("," , "|") + "," + shipping + "\n")

f.close()