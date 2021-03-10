import requests
from bs4 import BeautifulSoup
 
url = 'https://www.timeanddate.com/weather/'
 
res = requests.get(url).content
soup = BeautifulSoup(res,'html.parser')
 
data = soup.find('span',class_='my-city__city')
data1 = soup.find('span',class_='my-city__temp')
print(data.text)
print(data1.text)