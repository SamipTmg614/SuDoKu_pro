hello every one,
This is the program i have writeen as to propose my idea for upcoming software design project.
since we have studied only upto conditional statement, I wrote the codes by only using logical state ments.

this is basically supposed to be a 9x9 grid sudoku puzzle where few numbers are generated randomly.
Since the pattern is generalted randomly and input by the user can be done at any position if it satisfy the given conditions, the number gets added and at the end, this has result to not have a complete solution most of the time.

OVERVIEW:
there are 3 files i have made which have different functions but works according to each other.you have to run the main.py file. 
The main file has the codes which decides what a user can see and takes input from themn and as well as works to solve the problem if called.
the main file file is connected to check number where the position o the number to be input and the number is checked if it is available or not,if the number is available it returns available and replaces the given position with number.
where as all the data to work with or the place to store are made in data file for clarity and to make code understandable


how the decisiion process works:
on file data.py data is stored as list. WHen the print numbers is called in main.py random position as well as number is generated whis is sent to the check_number() function of checknumber file which replaces the given position of row set with the given number, this process is repeated for given range number of times.