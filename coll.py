from collections import Counter
from collections import namedtuple
from collections import defaultdict

ages = [22, 22, 25, 25, 30, 24, 26, 24, 35, 45, 52, 22, 22, 22, 25, 16, 11, 15, 40, 30]
value_counts = Counter(ages)
value_most_common = value_counts.most_common()

print(ages, "\n")
print(value_counts, "\n")
print(value_most_common, "\n")
print("age0", ages[-1])
print("value_most_common0", value_most_common[-1], "\n")



Features = namedtuple('Features', ['age', 'gender', 'name'])

row = Features(age=22, gender='male', name='Alex')
# print(Features)
print(row)
print(row.age)

data = 'the red fox ran as fast as it could'

my_default_dict1 = defaultdict(int)
print("1",my_default_dict1)
for letter in data:
	# print("letter", letter)
	my_default_dict1[letter] += 1
print("2",my_default_dict1)

my_default_dict2 = dict()
print("3",my_default_dict2)
for letter2 in data:
    my_default_dict2[letter2] = my_default_dict2.get(letter2,0) + 1
print("4",my_default_dict2)

new = {}
for key, value in data:
    group = new.setdefault(key, []) # key might exist already
    group.append(value)
    print("value", value, "group", group)