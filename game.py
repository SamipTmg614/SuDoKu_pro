import  sys , pygame as pg
import random 


pg.init()
screen_size = 750,750
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None,80)


number_grid = [
    ['','','','','','','','','',''],
    ['','','','','','','','','',''],
    ['','','','','','','','','',''],
    ['','','','','','','','','',''],
    ['','','','','','','','','',''],
    ['','','','','','','','','',''],
    ['','','','','','','','','',''],
    ['','','','','','','','','',''],
    ['','','','','','','','','',''],
               ]

def draw_background():
    screen.fill(pg.Color("white"))
    pg.draw.rect(screen , pg.Color("black"),pg.Rect(15,15,720,720),10)
    i = 1
    while (i*80)<720:
        if i%3==0:
            linewidth = 10
        else:
            linewidth = 5
        pg.draw.line(screen,pg.Color("black"),pg.Vector2((i * 80)+15,15),pg.Vector2((i*80)+15,735),linewidth)
        pg.draw.line(screen,pg.Color("black"),pg.Vector2(15 , (i * 80)+15),pg.Vector2(735,(i*80)+15),linewidth)
        i+=1

def Draw_numbers():
    numbers = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        for j in range(9):
            number = number_grid[i][j]
            n_text = font.render(str(number),True,pg.Color('black'))
            screen.blit(n_text, pg.Vector2(i*80 +35,j*80 +35) )


def Game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    draw_background()
    Draw_numbers()
    pg.display.flip()  



while 1:
    Game_loop()
     