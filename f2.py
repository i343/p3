import f1

print("File2 one __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File2 one executed when ran directly")
else:
   print("File2 one executed when imported")