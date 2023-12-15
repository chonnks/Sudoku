#Bruce Reyes
#INST126
#This is a sudoku puzzle solver
#I used documentation from stackoverflow and computerphile's video 
#but every part of the code can and will be explained

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

#algorithm that actually solves the sudoku board
def SudokuSolve(grid):
    FindSolution = FindSquare(grid)
    if not FindSolution: 
        return True # means that we found solution
    else:
        row, column = FindSolution
    
    for i in range (1,10): #excludes zero and goes 1-9
        if ValidBoard(grid, i, (row, column)): # if we add them into the board, they will be valid
            grid[row][column] = i

            if SudokuSolve(grid):
                return True
            
            grid[row][column] = 0 #backtracks  to last element and tries with different element 
    
    return False    


#function to find if current board is valid in terms of sudoku
def ValidBoard(grid, number, position):
    #checking row using loops
    for i in range(len(grid[0])):
        if grid[position[0]][i] == number and position[1] != i: #scan if number is in row, if it is just avoid that row 
            return False

    #checking column using same loop
    for i in range(len(grid[0])):
        if grid[i][position[1]] == number and position[0] != i: #scan if number is in column, if it is just avoid that column
            return False
    
    # Check the 3x3 box
    # allows each box to have a specific coordinate (0,0), (0,1) etc.
    BoxRow = position[1] // 3
    BoxColumn = position[0] // 3

    #loop through all elements in box
    for i in range(BoxColumn * 3, BoxColumn * 3 + 3): 
        for j in range(BoxRow * 3, BoxRow * 3 + 3): #this find what box we're in and multiplies to get to index values
            if grid[i][j] == number and (i,j) != position: # if number is already found in box, we do not have to go into box
                return False

    return True



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

    return None #if there are no zeroes then it will return FindSolution

print("Non-Solved Board\n")
PrintGrid(SudokuGrid) # prints before solving
SudokuSolve(SudokuGrid)
print("Solved Board\n")
PrintGrid(SudokuGrid) #prints after to show before and after


    
    