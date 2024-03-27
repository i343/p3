import requests
from bs4 import BeautifulSoup

# url = 'https://www.olx.com.eg/en/vehicles/cars-for-sale/'
url0 = 'https://'
url1 = 'www.' 
url2 = 'o' 
url3 = 'l' 
url4 = 'x.' 
url5 = 'u' 
url6 = 'a/' 
url7 = 'uslugi/delovye-uslugi/' 
url =   url0 + url1 + url2 +  url3 + url4 + url5 + url6 + url7 
print ('url ->', url)

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

print (soup)