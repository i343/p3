from ip2geotools.databases.noncommercial import DbIpCity

myip = ''

responseIP = DbIpCity.get(myip, api_key='free')

print(responseIP)
print()
print(responseIP.latitude,responseIP.longitude)
