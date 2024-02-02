import os

def digitize(Number):
    # print("start digitize")
    # print(Number)
    Number2String = str(Number)
    # print(Number2String)

    Map2Number2String = map(int,Number2String)
    # print(Map2Number2String)

    # print("stop digitize")
    return list(Map2Number2String)

def devision11(Number11):
    ArrayNumber11 = digitize(Number11)
    # print("start dev11")
    # for indexArrayNumber11 in ArrayNumber11:
    #     print(indexArrayNumber11)
    sign11 = 1
    SumNumber11 = 0
    print("start re dev11")   
    for indexArrayNumber11 in reversed(ArrayNumber11):
        SumNumber11 = SumNumber11 + sign11 * indexArrayNumber11
        if sign11 == 1: 
            sign11 = -1
        else :
            sign11 = 1
        print(SumNumber11)
    # print("stop dev11")

    return SumNumber11

os.system('clear')


# Numberic 11
print("\n\n\n###\n\n\n")
print("Devide a number into individual digits.")

InputNumberic11=int(input("Number: "))
InputNumberic = InputNumberic11*11
print("11 *", InputNumberic11," = ", InputNumberic)
print(" -> ",digitize(InputNumberic))
print("\n",devision11(InputNumberic))
print("rem: ",InputNumberic%11)