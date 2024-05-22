def check(x,y):
    if (x,y)==(0,0) or (x,y)==(0,1) or (x,y)==(0,2)or (x,y)==(1,0)or (x,y)==(1,1)or (x,y)==(1,2)or (x,y)==(2,0)or (x,y)==(2,1)or (x,y)==(2,2):
        result=0
        return result
    elif (x,y)==(0,3) or (x,y)==(0,4) or (x,y)==(0,5)or (x,y)==(1,3)or (x,y)==(1,4)or (x,y)==(1,5)or (x,y)==(2,3)or (x,y)==(2,4)or (x,y)==(2,5):
        result=1
        return result
    elif (x,y)==(0,6) or (x,y)==(0,7) or (x,y)==(0,8) or (x,y)==(1,6) or (x,y)==(1,7) or (x,y)==(1,8) or (x,y)==(2,6) or (x,y)==(2,7) or (x,y)==(2,8):
        result=2
        return result
    elif (x,y)==(3,0) or (x,y)==(3,1) or (x,y)==(3,1) or (x,y)==(4,0) or (x,y)==(4,1) or (x,y)==(4,2) or (x,y)==(5,0) or (x,y)==(5,1) or (x,y)==(5,2):
        result=3
        return result
    elif (x,y)==(3,3) or (x,y)==(3,4) or (x,y)==(3,5) or (x,y)==(4,3) or (x,y)==(4,4) or (x,y)==(4,5) or (x,y)==(5,3) or (x,y)==(5,4) or (x,y)==(5,5):
        result=4
        return result
    elif (x,y)==(3,6) or (x,y)==(3,7) or (x,y)==(3,8) or (x,y)==(4,6) or (x,y)==(4,7) or (x,y)==(4,8) or (x,y)==(5,6) or (x,y)==(5,7) or (x,y)==(5,8):
        result=5
        return result
    elif (x,y)==(6,0) or (x,y)==(6,1) or (x,y)==(6,2) or (x,y)==(7,0) or (x,y)==(7,1) or (x,y)==(7,2) or (x,y)==(8,0) or (x,y)==(8,1) or (x,y)==(8,2):
        result=6
        return result
    elif (x,y)==(6,3) or (x,y)==(6,4) or (x,y)==(6,5) or (x,y)==(7,3) or (x,y)==(7,4) or (x,y)==(7,5) or (x,y)==(8,3) or (x,y)==(8,4) or (x,y)==(8,5):
        result=7
        return result
    elif (x,y)==(6,6) or (x,y)==(6,7) or (x,y)==(6,8) or (x,y)==(7,6) or (x,y)==(7,7) or (x,y)==(7,8) or (x,y)==(8,6) or (x,y)==(8,7) or (x,y)==(8,8):
        result=8
        return result