
import  sys , pygame as pg
import random 
import checknum
import question

pg.init()
clock = pg.time.set_timer(pg.USEREVENT,1000)
screen_size = 750,800
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None,80)

selected_cell = None
number_grid = question.row
check = question.row

difficulty_levels = ['Easy', 'Medium', 'Hard']
selected_difficulty = None

def draw_background():
    screen.fill(pg.Color("black"))
    background_image=pg.image.load("b_9.jpg")
    background_image = pg.transform.scale(background_image, screen.get_size())
    screen.blit(background_image,(0,0))
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

def draw_buttons():
    # image=pg.image.load("button_background.png") #For Button Image
    button_width = 130
    button_height = 30
    font_size = 30  
    font_path="FreeSans.ttf"
    font = pg.font.Font(font_path, font_size)
    x = 20
    y = 750
    for i, level in enumerate(difficulty_levels):        
        button_rect = pg.Rect(x,y, button_width, button_height)
        pg.draw.rect(screen, pg.Color("black"), button_rect)
        text = font.render(level, True, pg.Color('grey'))
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)
        x += button_width +150


def Draw_numbers():
    for i in range(9):
        for j in range(9):
            number = number_grid[i][j]
            if number != '':
                # Calculate the position of each number
                text = font.render(str(number), True, pg.Color('black'))
                text_rect = text.get_rect(center=(j*80 + 15 + 40, i*80 + 15 + 40))
                screen.blit(text, text_rect)
def get_numbers():
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.unicode.isdigit():  # Check if the pressed key is a digit
                input_number = int(event.unicode)
                return input_number  # Return the input number if it's a digit
    return None  # Return None if no valid input is detected

def get_clicked_cell(mouse_pos):
    x, y = mouse_pos
    if 15 <= x <= 735 and 15 <= y <= 735:  # Check if mouse position is within the Sudoku grid
        col = (x - 15) // 80
        row = (y - 15) // 80
        return (row, col)
    else:
        return None 


def draw_selected_cell():
    global selected_cell
    if selected_cell is not None:
        # Draw a highlight around the selected cell
        row, col = selected_cell
        cell_rect = pg.Rect(15 + col * 80, 15 + row * 80, 80, 80)
        pg.draw.rect(screen, pg.Color("green"), cell_rect, 3)


def Game_loop():
    global number_grid
    global selected_cell
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos =pg.mouse.get_pos()
            selected_cell = get_clicked_cell(mouse_pos)
            x,y = mouse_pos
            if y>739:
                if x<145:
                    difficulty = "Easy"
                    question.change_row(difficulty)  
                elif x>=145 and x<450:
                    difficulty = "Medium"
                    question.change_row(difficulty)
                elif x>=450 and x<650:
                    difficulty = "Hard"
                    question.change_row(difficulty)
                
                
            number_grid = question.row

            Draw_numbers()
        elif event.type == pg.KEYDOWN:
            if selected_cell is not None and event.unicode.isdigit():
                row,col = selected_cell
                checknum.in_number(row,col,event.unicode,number_grid)
                if checknum.available==True:
                    number_grid[row][col] = int(event.unicode)
                selected_cell = None
    input_number = get_numbers()
    if input_number is not None:
        checknum.in_number()
        pg.display.flip()  

    draw_background()
    draw_buttons()

    draw_selected_cell()
    Draw_numbers()
    pg.display.flip()  
    pg.display.update()


while 1:
    Game_loop()
     
