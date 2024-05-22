import data
import check_box
row = data.row
col = data.col


available = None

def in_number(x,y,z):
    box_num=check_box.check(x,y)#Assigns the box number according to position
    box_data=data.box(box_num) #List that has all other elements in the respective box  
    
    if row[x][y] =='':
        if box_data is not None:
            if z not in row[x]:
                if z not in col[y]:
                    if z not in box_data:                   
                            row[x][y]=z
                            col[y][x]=z
                            box_data[box_num]=z
                            available = True
                    else:
                        available = False
                else:
                    available = False
            else:
                available = False
                
            return available
                