import question
col = [
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
row=question.row
for i in range(9):
    for j in range(9):
       col[i][j]=row[j][i]

def box(x):
    if x==0:
        box1 = [row[0][0],row[0][1],row[0][2],row[1][0],row[1][1],row[1][2],row[2][0],row[2][1],row[2][2]]
        return box1
    elif x==1:
        box2 = [row[0][3],row[0][4],row[0][5],row[1][3],row[1][4],row[1][5],row[2][3],row[2][4],row[2][5]]
        return box2
    elif x==2:
        box3=[row[0][6],row[0][7],row[0][8],row[1][6],row[1][7],row[1][8],row[2][6],row[2][7],row[2][8]]
        return box3
    elif x==3:
        box4=[row[3][0],row[3][1],row[3][2],row[4][0],row[4][1],row[4][2],row[5][0],row[5][1],row[5][2]]
        return box4
    elif x==4:
        box5=[row[3][3],row[3][4],row[3][5],row[4][3],row[4][4],row[4][5],row[5][3],row[5][4],row[5][5]]
        return box5
    elif x==5:
        box6=[row[3][6],row[3][7],row[3][8],row[4][6],row[4][7],row[4][8],row[5][6],row[5][7],row[5][8]]
        return box6
    elif x==6:
        box7=[row[6][0],row[6][1],row[6][2],row[7][0],row[7][1],row[7][2],row[8][0],row[8][1],row[8][2]]
        return box7
    elif x==7:
         box8=[row[6][3],row[6][4],row[6][5],row[7][3],row[7][4],row[7][5],row[8][3],row[8][4],row[8][5]]
         return box8
    elif x==8:
        box9=[row[6][6],row[6][7],row[6][8],row[7][6],row[7][7],row[7][8],row[8][6],row[8][7],row[8][8]]
        return box9
