import collections

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
listCM = list(collections.ChainMap(adjustments, baseline))

print(baseline)
print(adjustments)
print(listCM)
