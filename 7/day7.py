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

#part2


def check_equation_2(result, operands):
    #print(result,operands)
    multipliable = False
    addable = False
    concatenatable = False
    active_operand = operands[len(operands)-1]
    
    if len(operands) == 1:
        #print(active_operand == result)
        return active_operand == result
    if result % active_operand == 0:
        multipliable = check_equation_2(int(result/active_operand), operands[0:len(operands)-1])
    if result - active_operand > 0:
        addable = check_equation_2(result - active_operand, operands[0:len(operands)-1])
    s_result = str(result)
    s_operand = str(active_operand)
    if s_result[len(s_result)- len(s_operand):len(s_result)] == s_operand and len(s_result) > len(s_operand):
        new_result = int(s_result[0:len(s_result)-len(s_operand)])
        
        concatenatable = check_equation_2(new_result, operands[0:len(operands)-1])
    if addable or multipliable or concatenatable:
        return True
    return False

sum_2 = 0
for equation in equations:
    if check_equation_2(equation[0],equation[1]):
        sum_2 += equation[0]
        #print("approved!")

print("final result part2: " + str(sum_2))