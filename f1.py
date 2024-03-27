print("File1 two __name__ is set to: {}" .format(__name__))


if __name__ == "__main__":
   print("File1 one executed when ran directly")
else:
   print("File1 one executed when imported")
   