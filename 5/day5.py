with open("5/input", "r") as file:
    input = file.readlines()

rules = []
updates = []

for line in input:
    if "|" in line:
        rules.append(line.replace("\n", ""))
    if "," in line:
        updates.append(line.replace("\n", "").split(","))



def check_succesors(page, successors):
    for successor in successors:
        reverserule = successor + "|" + page
        if reverserule in rules:
           return False
    return True 

def check_update(update):
    for i in range(len(update)):
        successors = update[i+1:len(update)]
        if not check_succesors(update[i], successors):
            return False
    return True

sum = 0

for update in updates:
    if check_update(update):
        sum += int(update[int(len(update)/2)])

print(sum)
