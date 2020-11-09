import requests
from bs4 import BeautifulSoup

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
keyword = 'iphone'
pagenumber = '1'
results = []

#prints to limit
for i in range(1,11):
#r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword, headers=headers)
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn='+str(i), headers=headers)
    print('status code =', r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')

    boxes = soup.select('.clearfix.s-item__info')
    for box in boxes:
        #print('---')
        result = {}
        titles = box.select('.s-item__title--has-tags.s-item__title')
        for title in titles:
            #print('item=', title.text)
            result['title'] = title.text
        prices = box.select('.s-item__price')
        for price in prices:
            #print('price=', price.text)
            result['price'] = price.text
        status = box.select('.SECONDARY_INFO')
        for stat in status:
            #print('status=', stat.text)
            result['stat'] = stat.text
        # not just item and price, but status
        #print('results',result)
        results.append(result)

    print('len(results)=',len(results))


#not just item and price, but status


import json
j = json.dumps(results)
with open('items.json','w') as f:
    f.write(j)
print('j=',j)