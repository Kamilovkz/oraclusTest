from cgitb import reset
import requests
from django.shortcuts import render

def index(request):
    
    appId = 'AXJCAMW4DHQ3K7V3W2TZ2ZMGJ6QSVDU2F6'
    url = 'https://api.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=' + appId
    url2 = 'https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest&apikey=' + appId
    address = '0x71709946635796197767dEe2b60a6df47d55F6E0'

    res = requests.get(url.format(address)).json()
    res2 = requests.get(url2.format(address))
    print(res2.text)

    address_info = { 
        'address': res["result"][0]["from"],
        'to': res["result"][0]["to"],
        'value': res["result"][0]["value"],
    }
    
    #for status in info["statuses"]:
    #print('Status 1:', status["text"].encode("utf-8"))

    context = {
        'info': address_info 
        }

    return render(request, 'oraclus/index.html', context)
