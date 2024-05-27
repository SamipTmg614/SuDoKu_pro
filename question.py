import data
import checknum
import random
global random_number
random_number=random.randint(1,10)
row=[
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ]

def change_box():
    box1 = [row[0][0],row[0][1],row[0][2],row[1][0],row[1][1],row[1][2],row[2][0],row[2][1],row[2][2]]
    box2 = [row[0][3],row[0][4],row[0][5],row[1][3],row[1][4],row[1][5],row[2][3],row[2][4],row[2][5]]
    box3=[row[0][6],row[0][7],row[0][8],row[1][6],row[1][7],row[1][8],row[2][6],row[2][7],row[2][8]]
    box4=[row[3][0],row[3][1],row[3][2],row[4][0],row[4][1],row[4][2],row[5][0],row[5][1],row[5][2]]
    box5=[row[3][3],row[3][4],row[3][5],row[4][3],row[4][4],row[4][5],row[5][3],row[5][4],row[5][5]]
    box6=[row[3][6],row[3][7],row[3][8],row[4][6],row[4][7],row[4][8],row[5][6],row[5][7],row[5][8]]
    box7=[row[6][0],row[6][1],row[6][2],row[7][0],row[7][1],row[7][2],row[8][0],row[8][1],row[8][2]]
    box8=[row[6][3],row[6][4],row[6][5],row[7][3],row[7][4],row[7][5],row[8][3],row[8][4],row[8][5]]
    box9=[row[6][6],row[6][7],row[6][8],row[7][6],row[7][7],row[7][8],row[8][6],row[8][7],row[8][8]]

    box=[box1,box2,box3,box4,box5,box6,box7,box8,box9]
    return box

def change_row(x):
    global row,random_number
    if x=="Easy":
        if random_number==1:
            row=[ 
            ['','','',  '','6','',   '','5','8'],
            ['','5','2',  '','','9',   '','7','4'],
            ['','7','8',  '','','',   '','',''],

            ['','3','',  '4','9','',   '5','8',''],
            ['','','5',  '','','',   '4','','7'],
            ['','6','7',  '','8','3',   '','','2'],

            ['','2','',  '9','3','',   '8','6','5'],
            ['','','9',  '','','8',   '','','3'],
            ['3','8','',  '','4','5',   '','9','1'],
                ]
        
        elif random_number==2:
            row = [
                ['','','7',  '','5','',   '','','3'],
                ['3','4','2',  '6','','',   '','',''],
                ['','6','',  '','','3',   '','','7'],

                ['','','9',  '','3','8',   '','6','4'],
                ['7','','4',  '1','','',   '5','','8'],
                ['6','','',  '4','','',   '1','','2'],

                ['9','','6',  '','','5',   '','7',''],
                ['','','',  '8','9','',   '2','','6'],
                ['','5','1',  '7','2','',   '3','','9'],
                    ]
        
        elif random_number==3:
            row= [
                ['9','1','',  '','','8',   '','2',''],
                ['','8','7',  '3','4','',   '9','','5'],
                ['2','5','',  '','9','7',   '','',''],

                ['','7','',  '','','5',   '','3',''],
                ['1','','2',  '','3','4',   '','','8'],
                ['','','8',  '2','','9',   '7','','4'],

                ['','','',  '','5','',   '3','',''],
                ['','','',  '','','3',   '2','','6'],
                ['3','4','',  '','2','6',   '8','','1'],
                    ]
        elif random_number==4:
            row=[
                ['3','','',  '','6','',   '4','','5'],
                ['','1','6',  '3','7','',   '','2','8'],
                ['4','9','',  '','','5',   '7','','3'],

                ['','2','',  '','','6',   '','5',''],
                ['7','5','4',  '2','','8',   '','9',''],
                ['1','','',  '7','','',   '','8',''],

                ['','4','',  '','3','',   '','',''],
                ['','7','5',  '6','4','9',   '8','',''],
                ['','3','',  '8','','',   '5','',''],
                    ]
        elif random_number==5:
            row=[
                ['4','','',  '','5','',   '','3','2'],
                ['','1','',  '','9','',   '7','','5'],
                ['7','5','3',  '','','4',   '1','9','6'],

                ['','','1',  '','7','',   '','',''],
                ['6','','9',  '','','1',   '2','5',''],
                ['','','',  '5','','',   '6','1','3'],

                ['3','','4',  '','','8',   '','','1'],
                ['','','',  '4','','',   '','7','8'],
                ['','','',  '7','6','3',   '','2','9'],
                    ]
        elif random_number==6:
            row=[
                ['','4','',  '6','','8',   '','',''],
                ['5','6','',  '9','','',   '','2',''],
                ['1','9','7',  '2','4','',   '3','',''],

                ['','8','',  '','9','7',   '','','1'],
                ['','3','',  '1','','6',   '','','5'],
                ['','','9',  '5','','3',   '4','6',''],

                ['','','',  '3','5','',   '1','','8'],
                ['','','',  '','6','',   '','4','3'],
                ['','7','3',  '','','9',   '6','','2'],
                    ]
        elif random_number==7:
            row=[
                ['3','','5',  '9','2','',   '','','8'],
                ['','2','6',  '8','5','1',   '','','3'],
                ['','','',  '','','',   '6','','2'],

                ['9','1','',  '','','',   '','',''],
                ['','8','7',  '3','','2',   '','1',''],
                ['','','4',  '','','7',   '3','8','6'],

                ['5','','8',  '2','','',   '','','7'],
                ['','6','2',  '','','4',   '8','9','5'],
                ['4','7','',  '','8','',   '','',''],
                    ]
        elif random_number==8:
            row=[
                ['3','','2',  '','8','',   '1','','5'],
                ['','','7',  '2','','',   '','6',''],
                ['5','','8',  '9','','',   '','4','7'],

                ['','8','',  '4','','',   '3','','2'],
                ['','3','',  '1','6','',   '','5','8'],
                ['','1','',  '5','','',   '6','7',''],

                ['','2','',  '3','4','5',   '','','1'],
                ['','','',  '','2','6',   '','','9'],
                ['','','',  '','9','',   '5','2','6'],
                    ]
        elif random_number==9:
            row=[
                ['','2','',  '','9','1',   '','','3'],
                ['7','','',  '3','4','5',   '','2',''],
                ['','','9',  '','','',   '8','',''],

                ['3','1','',  '4','','9',   '','','5'],
                ['6','','4',  '5','','',   '','','9'],
                ['','','8',  '1','','',   '7','',''],

                ['8','','3',  '','5','4',   '','','7'],
                ['','','5',  '','8','',   '','','2'],
                ['','4','7',  '','1','3',   '5','6',''],
                    ]
        elif random_number==10:
            row=[
                ['3','9','',  '','','2',   '','',''],
                ['','','7',  '','','4',   '8','',''],
                ['','','4',  '','5','',   '1','9','6'],

                ['6','7','2',  '1','','',   '','8','4'],
                ['','3','1',  '9','4','',   '','',''],
                ['','4','',  '7','','',   '6','','1'],

                ['9','2','',  '4','','3',   '5','6',''],
                ['','','3',  '5','','1',   '4','','9'],
                ['','','',  '','6','9',   '','',''],
                    ]
        
    elif x=="Medium":
        if random_number==1:
            row=[
                    ['5','','6',  '3','','4',   '','',''],
                    ['4','9','',  '','','5',   '7','6','3'],
                    ['','8','7',  '9','','2',   '','',''],

                    ['','2','3',  '4','','6',   '1','5',''],
                    ['','5','',  '','','8',   '','',''],
                    ['1','','',  '7','5','',   '','8',''],

                    ['2','7','5',  '6','','',   '8','',''],
                    ['','3','',  '8','','7',   '','','9'],
                    ['','','',  '','3','1',   '','7',''],
                    ]
        elif random_number==2:
                row=[
                    ['1','6','',  '','','',   '','7','3'],
                    ['','','',  '','','5',   '','','6'],
                    ['4','','8',  '','7','',   '','9',''],

                    ['','8','',  '','','',   '','4',''],
                    ['','','',  '8','6','',   '','','9'],
                    ['3','','6',  '5','','9',   '','',''],

                    ['6','9','',  '7','5','4',   '8','','2'],
                    ['','','',  '','','3',   '1','','4'],
                    ['2','3','4',  '6','1','',   '9','','7'],
                    ]
        elif random_number==3:
                row=[
                    ['','','',  '5','1','',   '','3',''],
                    ['3','9','1',  '6','7','',   '5','','2'],
                    ['6','2','',  '8','9','',   '4','1','7'],

                    ['','3','2',  '','','',   '','6','4'],
                    ['','','',  '','6','',   '2','','8'],
                    ['8','','',  '','','1',   '','',''],

                    ['2','5','',  '','3','7',   '','',''],
                    ['','1','8',  '','','6',   '7','',''],
                    ['','','',  '','2','',   '','4',''],
                ]
        elif random_number==4:
                row=[
                    ['','','',  '','5','1',   '','6','2'],
                    ['','4','',  '','2','',   '','',''],
                    ['1','','',  '','','3',   '8','7',''],

                    ['4','7','1',  '8','9','',   '','2','3'],
                    ['6','','',  '3','1','',   '7','9','5'],
                    ['','5','',  '6','7','',   '','',''],

                    ['','3','4',  '','','',   '2','5',''],
                    ['2','','8',  '','3','',   '','',''],
                    ['','','',  '','','7',   '','','8'],
                ]
        elif random_number==5:
                row=[
                    ['4','','',  '','','',   '','1',''],
                    ['','','',  '','6','9',   '5','','8'],
                    ['','6','',  '5','','1',   '','',''],

                    ['','2','6',  '7','','5',   '4','8','3'],
                    ['','4','7',  '','8','',   '','',''],
                    ['','3','1',  '9','4','2',   '','6','5'],

                    ['6','','',  '2','','',   '1','','4'],
                    ['2','8','',  '','','',   '','5','7'],
                    ['','5','',  '','9','',   '','',''],
                ]
        elif random_number==6:
                row=[
                    ['','3','5',  '','2','',   '','',''],
                    ['9','','',  '','','8',   '','5','7'],
                    ['7','','8',  '4','9','',   '6','',''],

                    ['6','','4',  '','7','',   '','3',''],
                    ['8','','2',  '','6','3',   '7','',''],
                    ['3','5','',  '8','4','',   '','9',''],

                    ['4','7','',  '2','8','',   '','6',''],
                    ['','','',  '1','5','',   '','7',''],
                    ['','','',  '6','3','',   '4','2',''],
                ]
        elif random_number==7:
                row=[
                    ['6','1','5',  '8','3','',   '','4','9'],
                    ['3','','4',  '2','9','1',   '','7','6'],
                    ['','','',  '','','5',   '','8','1'],

                    ['','','7',  '','','',   '1','',''],
                    ['5','3','',  '','2','4',   '','',''],
                    ['','','',  '3','7','',   '','','4'],

                    ['8','','3',  '','','',   '9','','5'],
                    ['1','7','',  '9','','',   '4','',''],
                    ['','','',  '','','2',   '','','3'],
                ]
        elif random_number==8:
                row=[
                    ['7','','4',  '1','','2',   '','','5'],
                    ['','','',  '','7','9',   '2','','1'],
                    ['2','1','',  '5','3','8',   '','','7'],

                    ['','','',  '','8','7',   '5','1','9'],
                    ['','6','8',  '','','',   '','',''],
                    ['','9','7',  '2','5','4',   '3','',''],

                    ['','','',  '','4','5',   '1','7','8'],
                    ['','7','3',  '','','',   '6','',''],
                    ['','5','',  '','','',   '','','3'],
                ]
        elif random_number==9:
                row=[
                    ['','','8',  '','','',   '','7',''],
                    ['','','',  '3','','4',   '1','','2'],
                    ['','3','',  '','1','7',   '','',''],

                    ['','2','5',  '','','',   '','1','9'],
                    ['','','3',  '','5','',   '7','','8'],
                    ['','1','',  '4','','',   '','',''],

                    ['3','5','',  '','9','1',   '8','2','6'],
                    ['9','8','',  '2','','',   '','',''],
                    ['7','6','',  '8','4','5',   '','3','1'],
                ]
        elif random_number==10:
                row=[
                    ['','','3',  '','','5',   '','',''],
                    ['','9','8',  '','','',   '','3','4'],
                    ['','6','',  '9','','',   '1','','2'],

                    ['1','','7',  '5','9','2',   '','6','3'],
                    ['4','','2',  '','','8',   '','',''],
                    ['6','','9',  '4','3','',   '2','8','7'],

                    ['','2','',  '','','',   '','1',''],
                    ['','','',  '','5','6',   '3','','8'],
                    ['','','6',  '3','1','',   '','',''],
                ]
 
    elif x=="Hard":
        if random_number==1:
            row=[
                ['5','','',  '','','',   '6','','2'],
                ['','2','7',  '6','','3',   '','4',''],
                ['6','','',  '2','','7',   '','','1'],

                ['','','',  '','','2',   '','','7'],
                ['','1','',  '','4','5',   '','',''],
                ['','','',  '1','9','',   '','8','4'],

                ['1','','',  '4','','',   '','','7'],
                ['9','','',  '3','','',   '','',''],
                ['','','4',  '','6','1',   '','8','4'],
            ]
        elif random_number==2:
            row=[
                ['','','',  '5','6','',   '','7',''],
                ['4','5','',  '','9','7',   '','',''],
                ['','','6',  '','','',   '','','1'],

                ['5','4','',  '9','','',   '','','7'],
                ['','','',  '','','',   '','9','4'],
                ['1','9','',  '','7','3',   '','',''],

                ['','7','4',  '','','',   '1','','3'],
                ['2','','',  '','','',   '','','9'],
                ['','','',  '2','1','',   '','','6'],
            ]
        elif random_number==3:
            row=[
                ['7','','',  '9','','',   '','1',''],
                ['2','4','9',  '','','',   '','',''],
                ['','','',  '','','4',   '8','2','9'],

                ['1','','',  '','','',   '','','5'],
                ['','','',  '6','','9',   '','3',''],
                ['','','4',  '5','','',   '2','','6'],

                ['3','','',  '','','',   '7','5','1'],
                ['','7','',  '','1','',   '','9','3'],
                ['9','','',  '','5','',   '','8',''],
            ]
        elif random_number==4:
            row=[
                ['','1','',  '','','',   '4','7',''],
                ['','','',  '','','5',   '3','',''],
                ['7','','',  '2','','8',   '9','',''],

                ['','','',  '','2','7',   '','9','4'],
                ['','2','',  '5','9','',   '','','3'],
                ['','4','',  '8','1','3',   '','',''],

                ['9','','',  '','','',   '','','8'],
                ['1','','',  '7','3','',   '','',''],
                ['3','','',  '','','2',   '6','5',''],
            ]
        elif random_number==5:
            row=[
                ['2','','',  '','','8',   '','',''],
                ['','9','',  '','4','',   '','8','7'],
                ['8','','',  '','','7',   '','5','4'],

                ['','1','',  '6','8','',   '','',''],
                ['9','','',  '7','','',   '1','',''],
                ['','','4',  '','1','',   '5','3',''],

                ['','','1',  '','2','',   '','',''],
                ['4','','',  '8','','1',   '','','6'],
                ['','','6',  '4','','3',   '8','',''],
            ]
        elif random_number==6:
            row=[
                ['','','',  '3','','',   '8','1',''],
                ['','','',  '8','','1',   '','','2'],
                ['','9','8',  '','','',   '','','7'],

                ['','1','9',  '','2','7',   '','8',''],
                ['7','','',  '','','',   '3','2',''],
                ['4','5','2',  '6','8','',   '','',''],

                ['','7','',  '','','',   '6','','8'],
                ['2','','',  '5','9','',   '','',''],
                ['','','',  '','','',   '2','9',''],
            ]
        elif random_number==7:
            row=[
                ['','','2',  '5','','8',   '','',''],
                ['','3','',  '','6','',   '','',''],
                ['5','','6',  '4','','',   '','3','2'],

                ['2','','3',  '','8','',   '9','1',''],
                ['','','1',  '2','','4',   '6','',''],
                ['','6','',  '','','',   '4','2','7'],

                ['','','',  '','','',   '8','7',''],
                ['','','',  '','','6',   '','4',''],
                ['','','',  '','9','1',   '','5',''],
            ]
    return row
        elif random_number==8:
            row=[
                ['','9','',  '','','2',   '','7',''],
                ['','','8',  '','','',   '','',''],
                ['','5','',  '1','','6',   '','','2'],

                ['','2','',  '','','',   '4','','5'],
                ['6','','9',  '','','7',   '','',''],
                ['','','',  '9','8','',   '','2',''],

                ['','','',  '','','8',   '','','4'],
                ['1','','5',  '','','',   '6','',''],
                ['','','',  '','6','',   '','','9'],
            ]
        elif random_number==9:
            row=[
                ['','','',  '7','8','',   '','','6'],
                ['','','',  '','','9',   '8','5',''],
                ['','','9',  '','2','',   '','',''],

                ['','','7',  '3','','',   '','8',''],
                ['1','','6',  '9','','',   '','3',''],
                ['','8','',  '','','4',   '','1','9'],

                ['','','1',  '2','4','7',   '','',''],
                ['','7','',  '1','','5',   '','4','2'],
                ['','4','',  '','6','',   '','',''],
            ]
        elif random_number==10:
            row=[
                ['','','',  '','6','',   '','3',''],
                ['1','6','',  '','7','4',   '','9',''],
                ['','','',  '','','9',   '','',''],

                ['','','',  '','5','8',   '4','2',''],
                ['','','7',  '','','2',   '','1',''],
                ['2','','4',  '9','','',   '6','',''],

                ['3','4','',  '','','',   '','',''],
                ['','2','6',  '5','8','',   '','',''],
                ['8','9','',  '7','4','3',   '','',''],
            ]
    return row