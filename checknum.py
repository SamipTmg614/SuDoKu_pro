import data,question
import check_box
row = question.row
col = data.col
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




available = None

def in_number(x,y,z,row): 
    box_num=check_box.check(x,y)
    box_data=question.change_box()
    if row[x][y] =='':
        if z not in row[x]:
            if z not in col[y]:
                if z not in box_data[box_num]:                   
                        row[x][y]=z
                        col[y][x]=z
                        box_data=z                        
                        available = True
                else:
                    available = False
            else:
                available = False
        else:
            available = False
        
        return available
     