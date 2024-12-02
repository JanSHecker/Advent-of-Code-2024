#part1
with open("1/input", "r") as file:
    input = file.readlines()


list1 = []
list2  = []

for line in range(0,len(input)):
    entrees = input[line].split()
    list1.append(int(entrees[0]))
    list2.append(int(entrees[1]))

list1.sort()
list2.sort()
sum_of_distances = 0

for i in range(0,len(input)):
    sum_of_distances += abs(list1[i]-list2[i])



print(sum_of_distances)


#part2 

total_similarity_score = 0

for id in list1:
    similarity_score = id * list2.count(id)
    total_similarity_score += similarity_score

print(total_similarity_score)