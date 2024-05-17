import data
row = data.row

def check_number(x,y):
    global available
    available = True
    if x < 10:
        prow = 0
        if x ==1:
            pcol =0
        elif x==2:
            pcol =1
        elif x==3:
            pcol =2
        elif x==4:
            pcol =3
        elif x==5:
            pcol = 4
        elif x==6:
            pcol = 5
        elif x==7:
            pcol = 6
        elif x==8:
            pcol = 7
        else:
            pcol = 8
    elif 18>x>9:
        prow = 1
        if x ==10:
            pcol =0
        elif x == 11:
            pcol = 1
        elif x==12:
            pcol =2
        elif x==13:
            pcol =3
        elif x==14:
            pcol =4
        elif x==15:
            pcol = 5
        elif x==16:
            pcol = 6
        elif x==17:
            pcol = 7
        else:
            pcol = 8
    elif 28>x>18:
        prow = 2
        if x ==19:
            pcol =0
        elif x == 20:
            pcol = 1
        elif x==21:
            pcol =2
        elif x==22:
            pcol =3
        elif x==23:
            pcol =4
        elif x==24:
            pcol = 5
        elif x==25:
            pcol = 6
        elif x==26:
            pcol = 7
        else:
            pcol = 8
    elif 28>x>18:
        prow = 2
        if x ==19:
            pcol =0
        elif x == 20:
            pcol = 1
        elif x==21:
            pcol =2
        elif x==22:
            pcol =3
        elif x==23:
            pcol =4
        elif x==24:
            pcol = 5
        elif x==25:
            pcol = 6
        elif x==26:
            pcol = 7
        else:
            pcol = 8

    if y not in row[prow]:
        row[prow][pcol]=y
    else:
        available = False
        print("invaid number input in wrong place")
    return available