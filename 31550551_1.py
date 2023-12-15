import requests
import time
import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
import time

#Name: Jean Torres-Rosario

while(True):
    print("working")

    response = requests.get('https://finance.yahoo.com/most-active')

    if response.status_code == 200:
        print("Success/OK\nCode: " + str(response))
    elif response.status_code == 301:
        print("Permanent Redirect\nCode: " + str(response))
        #break
    elif response.status_code == 302:
        print("Temporary Redirect\nCode: " + str(response))
        #break
    elif response.status_code == 304:
        print("Not Modified\nCode: " + str(response))
        #break
    elif response.status_code == 401:
        print("Unauthorized Access Error\nCode: " + str(response))
        #break
    elif response.status_code == 403:
        print("Forbidden\nCode: " + str(response))
        #break
    elif response.status_code == 404:
        print("Not Found\nCode: " + str(response))
        #break
    elif response.status_code == 405:
        print("Method Not Allowed\nCode: " + str(response))
        #break
    elif response.status_code == 501:
        print("Not Implemented\nCode: " + str(response))
        #break
    elif response.status_code == 502:
        print("Bad Gateway\nCode: " + str(response))
        #break
    elif response.status_coe == 503:
        print("Service Unavailable\nCode: " + str(response))
        #break
    elif response.status_core == 504:
        print("Gateway Timeout\nCode: " + str(response))
        #break

    html_page = BeautifulSoup(response.text, "html.parser")

    names = html_page.find_all("td", {"aria-label": "Name"})
    symbols = html_page.find_all("td", {"aria-label": "Symbol"})
    values = html_page.find_all("td", {"aria-label": "Price (Intraday)"})
    changes = html_page.find_all("td", {"aria-label": "Change"})
    volumes = html_page.find_all("td", {"aria-label": "Volume"})

    '''PYMONGO CODE'''

    myclient = MongoClient()

    databasenames = myclient.list_database_names()

    if 'jean_database' in databasenames:
        myclient.drop_database('jean_database')

    mydb = myclient["jean_database"]

    collection = mydb["jean_collection"]

    for i in range(25):
        stock = {
            "Index": i + 1,
            "Name": names[i].text,
            "Symbol": symbols[i].text,
            "Price (Introday)": values[i].text,
            "Change": changes[i].text,
            "Volume": volumes[i].text,
        }

        x = collection.insert_one(stock)

        print(x.inserted_id)

    time.sleep(180)


