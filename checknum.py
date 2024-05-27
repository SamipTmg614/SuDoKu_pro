import question
row = question.row
col=question.col

#Function that returns True when the number is not repeated in row, column and box
def in_number(x,y,z,row): 
    box_num=question.check(x,y) #To determine box number
    box_data=question.change_box()  #Calling change_box to update box values
    for i in range(9):#Changing column values
        for j in range(9):
            col[i][j]=row[j][i]
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