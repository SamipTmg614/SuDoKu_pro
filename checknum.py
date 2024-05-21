import data
row = data.row
col = data.col
pbox = data.box

available = None

def in_number(x,y,z):

    for i in data.obox1:
        if x  in i and y  in i:
            a=True

    if row[x][y] =='':
        if z not in row[x]:
            if z not in col[y]:
                if a == True:
                    row[x][y]=z
                    col[y][x]=z
                    available = True

                else:
                    available = False
            else:
                available = False
        else:
            available = False
    else:
        available = False
    
    return available
    