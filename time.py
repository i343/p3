from datetime import timedelta


# year = timedelta(days=365)

year = "00:01:55.302363"
yearTotal = year.total_seconds()

print(year)
print(yearTotal)

another_year = timedelta(weeks=40, days=84, hours=23,
                         minutes=50, seconds=600)
year == another_year
yearTotal = year.total_seconds()

print(year)
print(yearTotal)