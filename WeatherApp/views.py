from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup
import datetime
 
#web scraping
 
url = 'https://www.timeanddate.com/weather/'
res = requests.get(url).content
soup = BeautifulSoup(res,'html.parser')
 
#home view
def home(requests,soup=soup):
    date = datetime.datetime.today().date
    data = soup.find('span',class_='my-city__city')
    data1 = soup.find('span',class_='my-city__temp')
     
    city = data.text
    temp = data1.text
 
    return render(requests,'index.html',{'city':city,'temp':temp,'date':date})

