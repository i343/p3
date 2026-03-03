import datetime
from pysunnoaa import noaa
import requests
import json

# Киева примерно 
# 50.45, 30.52
# https://gml.noaa.gov/grad/solcalc/


# API Sunrise-Sunset: Получает точное время начала и конца навигационных сумерек 
# для Киева 

lat= '50.435000'
lng = '30.476667'
# date = '2025-08-18'
# now.strftime("%Y-%m-%d")

# latitudeKyiv = 50.44 # Latitude (+ to N)
# longitudeKyiv = 30.48 # Longitude (+ to E)

latitudeKyiv = float(lat) # Latitude (+ to N)
longitudeKyiv = float(lng) # Longitude (+ to E)


timezoneKyiv = 3 # Time Zone (+ to E)
# thedatetime = datetime.datetime(2010, 6, 21, 9, 54)
thedatetimeNow = datetime.datetime.now()
dateNow = thedatetimeNow.strftime("%Y-%m-%d")

yearNow = int(thedatetimeNow.strftime("%Y"))
monthNow = int(thedatetimeNow.strftime("%m"))
dayNow = int(thedatetimeNow.strftime("%d"))
datetime_now = datetime.datetime(yearNow,monthNow,dayNow)

altitude, azimuth = noaa.sunposition(
    latitudeKyiv, longitudeKyiv, timezoneKyiv, thedatetimeNow, atm_corr=True
)
print(f"Now: {altitude}, {azimuth}, \nthedatetimeNow {thedatetimeNow}, \ndataNow {dateNow}, \ndatatime {datetime.datetime(2025, 8, 18)} \ndatetime_now {datetime_now}")

sunriseKyiv = noaa.sunrise(latitudeKyiv, longitudeKyiv, timezoneKyiv, datetime_now)
sunsetKyiv = noaa.sunset(latitudeKyiv, longitudeKyiv, timezoneKyiv, datetime_now)
print(f"Kyiv Sunrise: {sunriseKyiv}")
print(f"Kyiv Sunset : {sunsetKyiv}")



# link = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date={date}"
link = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date={dateNow}&tzid=Europe/Kyiv"


response = requests.get(link)
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(dateNow, json.dumps(data, indent=4))


