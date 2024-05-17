import random
numbers =[1,2,3,4,5,6,7,8,9]

row = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    ]
col = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    ]
box = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    ]

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
    for i in range(8):
        print(row[i])

def print_numbers():
    number = random.choice(numbers)
    for i in range(1,17):
        pos = random.choice(range(1,82))
        print(pos)

def check_number(x,y):
    global available
    available = True
    if x < 10:
        prow = 0
        if x ==1:
            pcol =0
            if y not in row[prow]:
                row[prow][pcol]=y
            else:
                available = False
        elif x==2:
            pcol =1
            row[prow][pcol]=y
        elif x==3:
            pcol =2
            row[prow][pcol]=y
        elif x==4:
            pcol =3
            row[prow][pcol]=y
        elif x==5:
            pcol = 4
            row[prow][pcol]=y
        elif x==6:
            pcol = 5
            row[prow][pcol]=y
        elif x==7:
            pcol = 6
            row[prow][pcol]=y
        elif x==8:
            pcol = 7
            row[prow][pcol]=y
        else:
            pcol = 8
            row[prow][pcol]=y

    return available


def input_number():
    integer = int(input('enter your position: '))
    if integer>0 and integer<=81:
        inp = int(input("enter your number: "))
        if 0< inp <=9:
            check_number(integer,inp)
            if available == False:
                input_number()

for i in range(9):
    output()
    input_number()
    
