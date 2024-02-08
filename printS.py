import os

def chAudioDir():

    osName = os.name

    if osName == "posix":
        os.system('clear')
        # print("Start debug play sound.")
        print ("os name:", osName)
        print()
    else :
        os.system('cls')
        # print("Start debug play sound.")
        print ("os name:", osName)
        print()    
    pwdName = os.getcwd();
    print("path ->",pwdName,"\n") 
    # os.system('ls -alt')

chAudioDir()

verb1 = {
  "inf" : "be",
  "inf1": "was",
  "inf2": "were",
  "inf3": "been",
  "rate" : 2004
}

verb2 = {
  "inf" : "become",
  "rate" : 2007
}

verb3 = {
  "inf" : "do",
  "rate" : 2011
}

irrVerb = {
  "be" : verb1,
  "become" : verb2,
  "do" : verb3
}

print(irrVerb["be"]["inf"])
print(irrVerb["be"]["inf1"])
print(irrVerb["be"]["inf2"])
print(irrVerb["be"]["inf3"])
print(irrVerb["be"]["inf"])
print(irrVerb)

print("\nstart for irrVerb \n")
for indexIrrVerb in irrVerb:
  print(indexIrrVerb)
  print(irrVerb[indexIrrVerb])
  for indexVerb in irrVerb[indexIrrVerb]:
    print(indexVerb , " -> " , irrVerb[indexIrrVerb][indexVerb])
  print("---")
  
print(verb1)

myf = {
  "c1" : {
    "name" : "E",
    "year" : 2004
  },
  "c2" : {
    "name" : "T",
    "year" : 2007
  },
  "c3" : {
    "name" : "L",
    "year" : 2011
  }
}
print("stroka 62")
print(myf["c1"]["name"])
