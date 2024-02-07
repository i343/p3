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

c1 = {
  "name" : "Ee",
  "year" : 2004
}
c2 = {
  "name" : "Tt",
  "year" : 2007
}
c3 = {
  "name" : "lL",
  "year" : 2011
}

fm = {
  "ch1" : c1,
  "ch2" : c2,
  "ch3" : c3
}

print(fm["ch2"]["name"])

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

print(myf["c1"]["name"])
