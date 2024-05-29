#SUDOKU


hello every one,
This is the program we have writeen as for software design project.
this program focuses only on using basic python conditional statements to handle task.

this is a  9x9 grid sudoku puzzle where different numbers are generated on basis of level user choose .
The questions are taken from online so that the puzzel is solvable.

OVERVIEW:
on running the code, we get to see the empty grid where user can choose the question levels by clicking the 3 different levels.
onle level is selected, user can input the number in empty space which is displayed if coreect else not.


Gui:
as to present the program user friendly, we have used pygame module to pringt the window,grids,take input from user.
where as the decision making is handeled by conditional statement.

how the decisiion process works:
once user clicks on the empty grid and inputs a number, pygame checks if the inserted number is whether 1-9 or not.
when level is choosen. the datas for row,column and box are stored in seperate lists. Every grid is assigned certain values so when user inputs a number, it is checked whether that number is present in
given row or column box. If no similar number is found, the number gets updated to every lists for rows, column and boxes.
this process is done for every number user inserts into the grid untill puzzle is solved.
