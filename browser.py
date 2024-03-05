from socket import socket
from urllib3 import request

URL0 = "https://www.ukr.net/sdds"
URL1 =  "http://112122.ru/"

# resp = request("GET", URL1)

# print(resp.data)



try:
    resp = request("GET", URL1)
    print(resp.status)
except:
    print('error')
finally:
    print('Done.')
    
