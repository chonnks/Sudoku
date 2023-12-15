#Bruce Reyes
#INST126
#This is a sudoku puzzle solver
#i used documentation from stackoverflow and computerphile's video 
# but every part of the code can and will be explained

#grid for sudoku: 9x9  with prefilled number
SudokuGrid = [ #this is our starting board
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0 ,0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# function that actually prints out grid
def PrintGrid(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0: 
            print("- - - - - - - - - - - - - ") 
            #maps out horizontal line for after every 3 rows to make boxes  

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                #maps out vertical lines between every 3 columns

            if j == 8:
                print(grid[i][j]) # i and j commonly used for loop placeholders, they are used as row and column
            else:
                print(str(grid[i][j]) + " ", end="")

#function to find the empty square to find the correct number using loops
def FindSquare(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i,j) # row and column in empty square




    
    