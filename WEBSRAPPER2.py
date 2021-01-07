from selenium import webdriver
from bs4 import BeautifulSoup
import pandas 

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.hackerrank.com/dashboard")
content = driver.page_source
soup = BeautifulSoup(content)
t =  soup.findAll("div", attrs={'class':'track-name'})
#print(t)
L =[]
for i in t:
    L.append(i.text)
df = pandas.DataFrame({'Name':L})
df.to_excel('pro.xlsx', index= False)