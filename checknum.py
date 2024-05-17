import data
row = data.row
col = data.col
pbox = data.box

def check_number(x,y):
    global available
    available = True
    if x < 10:
        
        prow = 0
        if x ==1:
            pcol =0
            abox =0
        elif x==2:
            pcol =1
            abox = 1
        elif x==3:
            pcol =2
            abox = 2
        elif x==4:
            pcol =3
            abox = 0
        elif x==5:
            pcol = 4
            abox = 1
        elif x==6:
            pcol = 5
            abox = 2
        elif x==7:
            pcol = 6
            abox = 0
        elif x==8:
            abox=1
            pcol = 7
        else:
            abox=2
            pcol = 8
    elif 18>x>9:
        prow = 1
        if x ==10:
            pcol =0
            abox=3
        elif x == 11:
            pcol = 1
            abox=4
        elif x==12:
            abox=5
            pcol =2
        elif x==13:
            abox=3
            pcol =3
        elif x==14:
            abox=4
            pcol =4
        elif x==15:
            abox=5
            pcol = 5
        elif x==16:
            abox=3
            pcol = 6
        elif x==17:
            abox=4
            pcol = 7
        else:
            abox=5
            pcol = 8
    elif 28>x>18:
        prow = 2
        if x ==19:
            pcol =0
            abox =0
        elif x == 20:
            abox=7
            pcol = 1
        elif x==21:
            abox=8
            pcol =2
        elif x==22:
            abox=6
            pcol =3
        elif x==23:
            abox=7
            pcol =4
        elif x==24:
            abox=8
            pcol = 5
        elif x==25:
            abox=6
            pcol = 6
        elif x==26:
            abox=7
            pcol = 7
        else:
            abox=8
            pcol = 8
    elif 28<=x<37:
        prow = 3
        if x ==28:
            pcol =0
            abox = 0
        elif x == 29:
            abox = 1
            pcol = 1
        elif x==30:
            abox = 2
            pcol =2
        elif x==31:
            abox = 0
            pcol =3
        elif x==32:
            abox = 1
            pcol =4
        elif x==33:
            abox = 2
            pcol = 5
        elif x==34:
            abox = 0
            pcol = 6
        elif x==35:
            abox = 1
            pcol = 7
        else:
            abox = 2
            pcol = 8
    elif 37<=x<45:
        prow = 4
        if x ==37:
            abox = 3
            pcol =0
        elif x == 38:
            abox = 4
            pcol = 1
        elif x==39:
            abox = 5
            pcol =2
        elif x==40:
            abox = 3
            pcol =3
        elif x==41:
            abox = 4
            pcol =4
        elif x==42:
            abox = 5
            pcol = 5
        elif x==43:
            abox = 3
            pcol = 6
        elif x==44:
            abox = 4
            pcol = 7
        else:
            abox = 5
            pcol = 8
    elif 46<=x<54:
        prow = 5
        if x ==46:
            abox = 6
            pcol =0
        elif x ==47:
            abox = 7
            pcol = 1
        elif x==48:
            abox = 8
            pcol =2
        elif x==49:
            abox = 6
            pcol =3
        elif x==50:
            abox = 7
            pcol =4
        elif x==51:
            abox = 8
            pcol = 5
        elif x==52:
            abox = 6
            pcol = 6
        elif x==53:
            abox = 7
            pcol = 7
        else:
            abox = 8
            pcol = 8
    elif 55<=x<63:
        prow = 6
        if x ==55:
            abox = 0
            pcol =0
        elif x == 56:
            abox = 1
            pcol = 1
        elif x==57:
            abox = 2
            pcol =2
        elif x==58:
            abox = 0
            pcol =3
        elif x==59:
            abox = 1
            pcol =4
        elif x==60:
            abox = 2
            pcol = 5
        elif x==61:
            abox = 0
            pcol = 6
        elif x==62:
            abox = 1
            pcol = 7
        else:
            abox = 2
            pcol = 8
    elif 64<=x<72:
        prow = 7
        if x ==64:
            abox = 3
            pcol =0
        elif x == 65:
            abox = 4
            pcol = 1
        elif x==66:
            abox = 5
            pcol =2
        elif x==67:
            abox = 3
            pcol =3
        elif x==68:
            abox = 4
            pcol =4
        elif x==69:
            abox = 5
            pcol = 5
        elif x==70:
            abox = 3
            pcol = 6
        elif x==71:
            abox = 4
            pcol = 7
        else:
            abox = 5
            pcol = 8
    else:
        prow = 8
        if x ==73:
            abox = 6
            pcol =0
        elif x == 74:
            abox = 7
            pcol = 1
        elif x==75:
            abox = 8
            pcol =2
        elif x==76:
            pcol =3
            abox = 6
        elif x==77:
            pcol =4
            abox = 7
        elif x==78:
            pcol = 5
            abox = 8
        elif x==79:
            pcol = 6
            abox = 6
        elif x==80:
            pcol = 7
            abox = 7
        else:
            abox = 8
            pcol = 8

    if x in data.obox1:
        oabox = 0
    elif x in data.obox2:
        oabox = 1
    elif x in data.obox3:
        oabox = 2
    elif x in data.obox4:
        oabox = 3
    elif x in data.obox5:
        oabox = 4
    elif x in data.obox6:
        oabox = 5
    elif x in data.obox7:
        oabox = 6
    elif x in data.obox8:
        oabox = 7
    else:
        oabox = 8
    
    if row[prow][pcol] !=0:
        available = False
        print("cannot change fixed value!")
    if y not in row[prow]:
        if y not in col[pcol]:
            if y not in pbox[oabox]:
                row[prow][pcol]=y
                col[pcol][prow]=y
                pbox[oabox][abox]=y
            else:
                available = False
                print("invaid number input in wrong place")
        else:
            available = False
            print("invaid number input in wrong place")
    else:
        available = False
        print("invaid number input in wrong place")
    return available