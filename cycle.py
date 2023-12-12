import requests 
from bs4 import BeautifulSoup
import time

#while(True):
print("works")

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

#names = html_page.find_all("fin-streamer")
names = html_page.find_all("fin-streamer", {"aria-label": "Volume"})

#troll = names.find("value")

#values = []

#for value in names:
	
#	print(value)

print(names)

#time.sleep(10)


