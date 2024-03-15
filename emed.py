from urllib.request import urlopen

# request = 'https://api.ehealth.gov.ua/api/dictionaries'

request = "http://www.google.com"

response_body = urlopen(request).read()


print (response_body)

