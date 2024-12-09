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

#part2

def is_sorted_before(a,b):
    rule = a + "|" + b
    reverse_rule = b + "|" + a
    if rule in rules:
        return True
    if reverse_rule in rules:
        return False

def order_update(update):
    for i in range(1, len(update)):
        key = update[i]
        j = i - 1
        while j >= 0 and is_sorted_before(key,update[j]):
            update[j + 1] = update[j]
            j -= 1
        update[j + 1] = key
    return update


sum_2 = 0

for update in updates:
    if not check_update(update):
        ordered = order_update(update)
        sum_2 += int(ordered[int(len(ordered)/2)])

print(sum_2)