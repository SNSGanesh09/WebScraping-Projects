#import section
import pandas as p
import requests
import csv
from bs4 import BeautifulSoup

url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

response=requests.get(url)
#print(response)

soup=BeautifulSoup(response.content,"html.parser")
#print(soup)

titles=soup.find_all('div',class_='KzDlHZ')
#print(tittles)
ratings=soup.find_all('div',class_='XQDdHH')
#print(ratings)
reviews=soup.find_all('span',class_='Wphh3N')
#Print(reviews)
prices=soup.find_all('div',class_='hl05eU')
#print(prices)

mt=[]
mr=[]
mre=[]
mp=[]

for title,rating,review,price in zip(titles,ratings,reviews,prices):
    mt.append(title.text)
    mr.append(rating.text)
    mre.append(review.text)
    mp.append(price.text)

#saving data in CSV

d={'mt':mt,'mr':mr,'mre':mre,'mp':mp}
#print(d)

model=p.DataFrame(data=d)

model.to_csv("mobilesdata.csv")
