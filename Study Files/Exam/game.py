# this one

# Write a function, process_game(), which takes two arguments (filename; a string containing a valid path to a file, and a function argument handler; any function that takes a single string argument).  You can assume that the file exists.  This function will read the contents of that file, which will contain a single line of text.

# The contents of the file will be a single string consisting of 81 characters, all on a single line.  Each character can be one of '1', '2', '3', '4', '5', '6', '7', '8', '9', and ' ' (space) characters.  This data will represent the current state of a sudoku game, but don't worry!  You don't need to know how to play sudoku in order to solve this problem, nor do you have to write a program to solve a sudoku!  Once the file's contents have been loaded into a string variable, simply call the handler() function, passing this string as its argument.

# Write a function, print_game(), which takes a single argument (game_state, a string containing 81 '1', '2', '3', '4', '5', '6', '7', '8', '9', and ' ' (space) characters, with no spaces or newlines between them, and prints a 9x9 game board.  To do this, print every sequence of 9 characters, each on their own line, with a space in between each character.

# Write some test code to call process_game(), using a data file (an example file: game.txt) and the print_game() function as arguments.

#  2          6    3 74 8         3  2 8  4  1 6  5         1 78 5    9          4


def process_game(filename, handler):
    with open(filename, "r") as file:
        handler(file.read())


def print_game(game_state):
    for i in range(9):
        print(game_state[i * 9 : (i + 1) * 9])


process_game("game.txt", print_game)
