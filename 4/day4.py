with open("4/input", "r") as file:
    input = file.readlines()

#part 1

lines = len(input)
columns = len(input[0])

STRING_MAS = "MAS"

directions = [
   [1,0],
   [1,1],
   [0,1],
   [-1,1],
   [-1,0],
   [-1,-1],
   [0,-1],
   [1,-1],
]


def check_X_for_MAS(line, column, direction):
    x = column + direction[0]
    y = line + direction[1]

    for a in STRING_MAS:    
        if y < 0 or y >= lines or x < 0 or x >= columns:
            return False
        elif input[y][x] == a:
           x += direction[0]
           y += direction[1]
        else:
           return False
        
    return True



XMAS_occurences = 0

for line_no in range(lines):
 for column_no in range(columns):
    letter = input[line_no][column_no]
    if letter == "X":
       for dir in directions:
          if check_X_for_MAS(line_no,column_no , dir):
             XMAS_occurences += 1

print(XMAS_occurences)

#part 2

diagonals_only = [
   [1,1],
   [-1,1],
   [-1,-1],
   [1,-1],
]


def check_A_for_crossmass(line, column):
    for direction in diagonals_only:
        y = line + direction[1]
        x = column + direction[0]
        opp_y = line + direction[1] * -1
        opp_x = column + direction[0] * -1
        if y < 0 or y >= lines or x < 0 or x >= columns:
            return False
        if opp_y < 0 or opp_y >= lines or opp_x < 0 or opp_x >= columns:
            return False
        else:
           diag = input[y][x] + "A" + input[opp_y][opp_x]
           if  diag != "SAM" and diag != "MAS":
                return False
    return True

crossmas_occurences = 0

for line_no in range(lines):
 for column_no in range(columns):
    letter = input[line_no][column_no]
    if letter == "A":
        if check_A_for_crossmass(line_no,column_no):
            crossmas_occurences += 1

print(crossmas_occurences)