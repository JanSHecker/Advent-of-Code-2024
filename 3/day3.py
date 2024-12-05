import re

with open("3/input", "r") as file:
    input = file.read()

def compute(function):
    parts = re.split("[(,)]", function)
    sum = int(parts[1]) * int(parts[2])
    return sum

#part 1
multiplications = re.findall("mul[(][0-9]+[,][0-9]+[)]",input)

sum = 0

for multiplication in multiplications:
    sum +=compute(multiplication)
print(sum)

#part 2
commands = re.findall("mul[(][0-9]+[,][0-9]+[)]|do[(][)]|don[']t[(][)]", input)

sum2 = 0

multiplication_enabled = True
for command in commands:
    if "mul" in command:  
        if multiplication_enabled:  
            sum2 += compute(command)
    elif "don't()" in command: 
        multiplication_enabled = False
    elif "do()" in command:  
        multiplication_enabled = True       
print(sum2)
        