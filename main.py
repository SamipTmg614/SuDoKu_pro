import random
import checknum
import data
numbers =[1,2,3,4,5,6,7,8,9]


print("POSTIONS FOR YOUR CONVINIENCE")
print(" 1  2  3  4  5  6  7  8  9")
print("10 11 12 13 14 15 16 17 18")
print("19 20 21 22 23 24 25 26 27")
print("28 29 30 31 32 33 34 35 36")
print("37 38 39 40 41 42 43 44 45")
print("46 47 48 49 50 51 52 53 54")
print("55 56 57 58 59 60 61 62 63")
print("64 65 66 67 68 69 70 71 72")
print("73 74 75 76 77 78 79 80 81")
print("=======================================")

def output():
    for i in range(9):
        print(data.row[i])

def print_numbers():
    for i in range(30):
        number = random.choice(numbers)
        pos = random.choice(range(1,81))
        checknum.check_number(pos,number)
        
def solve_numbers():
    for i in range(999):
        number = random.choice(numbers)
        for j in range(1,82):
            pos = random.choice(range(1,82))
            checknum.check_number(pos,number)



def input_number():
    integer = int(input('enter your position: '))
    if integer == 669:
        solve_numbers()
        # output()
    if integer>0 and integer<=81:
        inp = int(input("enter your number: "))
        if 0< inp <=9:
            checknum.check_number(integer,inp)
            if checknum.available == False:
                print("invaid number input in wrong place")
                input_number()
            else:
                print("insert succesfull")
        else:
            print("number out of range")
            input_number()

    


print_numbers()
for i in range(200):
    output()
    input_number()

    
