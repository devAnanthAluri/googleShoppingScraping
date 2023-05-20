from bs4 import BeautifulSoup
import requests
import json
from configparser import ConfigParser
from openpyxl import  Workbook

def xl(d,s):
    wb = Workbook()
    sheet = wb.active 
    c = sheet['A1']
    c.value = "Name of the product"
    c = sheet['B1']
    c.value = "Price of the product"
    c = sheet['C1']
    c.value = "Link to the product"
    c = sheet['D1']
    c.value = "Supplier of the product"
    c = sheet['E1']
    c.value = "Delivery Service of the supplier"
    q=2
    w=1
    for i in d:
        w=1 
        for j in i.values():
            c = sheet.cell(row = q, column = w) 
            c.value = j
            w+=1
        q+=1
    filename="data_{q}.xlsx".format(q=s)
    wb.save(filename=filename)
    
def ext(s):
    headers = {  
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }
    
    config = ConfigParser()
    config.read('config.ini')
    ppr_min=config.get('searchOptions','ppr_min')
    ppr_max=config.get('searchOptions','ppr_max')
    ship=config.get('searchOptions','ship')
    p_ord=config.get('searchOptions','p_ord')

    url='https://www.google.com/search?q={key}&tbm=shop&tbs=mr:1,price:1,ppr_min:{q},ppr_max:{w},ship:{e},sales:1,p_ord:{r}'.format(key=s,q=ppr_min,w=ppr_max,e=ship,r=p_ord)
    response = requests.get(url,headers=headers).text
    print(url)

    soup = BeautifulSoup(response, 'html.parser')

    data = []

    for container in soup.findAll('div', class_='sh-dgr__content'):
        d={}
        title = container.find('h3', class_='tAxDx').text
        priced = container.find('span', class_='a8Pemb OFFNJ').text
        link=container.find('a', class_='shntl').get("href")
        supplier = container.find('div', class_='aULzUe IuHnof').text
        delivery = container.find('div', class_='vEjMR').text
        
        price=''
        for i in priced:
            if(i==' '): 
                break
            elif (i==','):
                pass
            else:
                price+=i

        price=int(float(price[1:]))
        if (delivery[0]=="\u20b9"):
            delivery=delivery[1:]

        d['title']=title
        d['price']=price
        d['link']="https://www.google.com"+link
        d['supplier']=supplier
        d['delivery']=delivery
        data.append(d)

    sortedData=sorted(data, key=lambda i: i['price'])

    #print(json.dumps(sortedData, indent=2, ensure_ascii=False))
    xl(sortedData,s)

    with open("data_{q}.json".format(q=s), "w") as file:
        json.dump(sortedData, file)

def configChanger():
    print("do you to change previous config to run(Y/n)")
    c=input().lower()

    if (c=='y'):
        '''
        ppr_min is minimum price
        ppr_max is maximum price
        ship:1 is free delivery
        p_ord:p is price low apple
        to high
        p_ord:pd is price high to low
        p_ord:r is prodects according to relevance  
        p_ord:rv is prodects according to review score
        full url: https://www.google.com/search?q=watch+kid&tbm=shop&tbs=mr:1,price:1,ppr_min:11,ppr_max:111,ship:1,sales:1,p_ord:r
        '''
        config=ConfigParser()
        config.read('config.ini')
        print("setting which can be changed minimum price(1), maximum price(2), shipping(3), product sort(4)")
        a=11
        while(a==11):
            w = int(input("what do u want to do \n = "))
            if(w==1):
                e=input("set new minimum price = ")
                config.set("searchOptions","ppr_min",e)
            elif(w==2):
                e=input("set new maximum price = ")
                config.set("searchOptions","ppr_max",e)
            elif(w==3):
                e=input("set free shipping(1) or not(0) = ")
                config.set("searchOptions","ship",e)
            elif(w==4):
                e=input("set new product sort: relevance(r), Review score(rv), Price - low to high(p),  Price - high to low(pd) = ")
                config.set("searchOptions","p_ord",e)
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            a=int(input("Do you want to continue yes(11) or no(22) = "))

q = input("Enter the item you want to search for = ")
configChanger()
ext(q)
