import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.alibaba.com/trade/search?spm=a27aq.cp_44.4746171840.1.afca3ccfxEij2Y&CatId=7&SearchText=Computer+Hardware+%26+Software&language=en&indexArea=product_en")
print(response)#it should out [200] means it succesful otherwise there is error
soup = BeautifulSoup(response.content,"html.parser")
#print(soup.prettify().encode("utf-8",errors="ignore"))#ouputs the contents of the page #code
d = soup.find("div",attrs={"class":"vc-carousel"})#finding details from a site
print(d)#outputs the contents of div class: vc-carousel