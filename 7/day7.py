with open("7/input", "r") as file:
    input = file.readlines()

equations = []

for line in input:
    line = line.replace("\n", "")
    split = line.split(": ")
    operands = split[1].split(" ")
    for i in range(len(operands)):
        operands[i] = int(operands[i])
    equations.append([int(split[0]),operands])

def check_equation(result, operands):
    multipliable = False
    addable = False
    active_operand = operands[len(operands)-1]
    if len(operands) == 1:
        return active_operand == result
    if result % active_operand == 0:
        multipliable = check_equation(result/active_operand, operands[0:len(operands)-1])
    addable = check_equation(result - active_operand, operands[0:len(operands)-1])
    if addable or multipliable:
        return True
    return False
sum = 0

for equation in equations:
    if check_equation(equation[0],equation[1]):
        sum += equation[0]


print("final result: " + str(sum))