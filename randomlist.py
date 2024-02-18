import random

spisok = ["Love", "World", "Peace", "Pypa",]

random.shuffle(spisok)
print (spisok)

words =  ["Alex", "Kate", "Love", "World", "Peace", "Pypa",]
print(words, "0")

unique_words = list(set(words))
print(unique_words,"1")

random.shuffle(unique_words) # shuffle using default Mersenne Twister generator
print(unique_words,"2")

random.SystemRandom().shuffle(unique_words)  # OS-provided generator
print(unique_words,"3")

# print("\n".join(unique_words))