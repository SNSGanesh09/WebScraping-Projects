#import section
import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup

url='https://www.bikewale.com/royalenfield-bikes/'

response=requests.get('https://www.bikewale.com/royalenfield-bikes/')
#print(response)

soup=BeautifulSoup(response.content,'html.parser')
#print(soup)

names=soup.find_all('h3',class_='o-jjpuv o-cVMLxW o-mHabQ o-fzpibK')
#print(names)

prices=soup.find_all('span',class_='o-eZTujG o-byFsZJ o-bkmzIL o-bVSleT')
#print(prices)


ratings=soup.find_all('div',class_='o-fzoTnS o-daXxmY o-wuqlZ o-BosvO o-fvgKOf o-fzqLoc o-bJruGr o-bsCSvY o-dMmXZk')
#print(ratings)


features=soup.find_all('span',class_='o-cNwRuH o-cQa-DfF')
#print(features)

bn=[]
bp=[]
br=[]
bf=[]

for name,price,rating,feature in zip(names,prices,ratings,features):
      bn.append(name.text)
      bp.append(price.text)
      br.append(rating.text)
      bf.append(feature.text)


models=pd.DataFrame()
#print(models)

data={"bn":bn,
      "bp":bp,
      "br":br,
      "bf":bf
      }
print(data)

models=pd.DataFrame(data)

models.to_csv("bike_models.csv")

