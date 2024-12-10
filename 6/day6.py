with open("6/input", "r") as file:
    input = file.readlines()

for i in range(len(input)):
    input[i] = input[i].replace("\n", "")

map_height = len(input)
map_width = len(input[0])

directions = [
    [0,-1], #up
    [1,0], #right
    [0, 1], #down
    [-1,0], #left
]

for i in range(len(input)):
    input[i] = input[i].replace("\n", "")

def find_guard():
    location = []
    for i in range(len(input)):
        if "^" in input[i]:
           location.append(input[i].find("^"))
           location.append(i)
    return location
    

location = find_guard()
d = 0
distinct_locations = [location]
onmap = True
while onmap:
    new_location = [location[0] + directions[d][0], location[1] + directions[d][1]]
    if new_location[0] >= 0 and new_location[0] < map_width and new_location[1] >= 0 and new_location[1] < map_height:
        new_tile = input[new_location[1]][new_location[0]]
        if new_tile == "." or new_tile == "^":
            #print("moving")
            location = new_location
            if not location in distinct_locations:
                distinct_locations.append(location)
            continue 
        if new_tile == "#":
            #print("turn right")
            d = (d+1)%4
            continue 
        raise Exception("unexpexted character")
    else: 
        onmap = False

print(len(distinct_locations))

#part2

def set_obstacle(string,w):
    char_list = list(string)
    char_list[w] = "#"
    modified_string = "".join(char_list)
    return modified_string

old_path = distinct_locations

potential_locations = []

for w in range(map_width):
    for h in range(map_height):
        if not (input[h][w] == "." and [w,h] in old_path):
            continue
        modified_input = input.copy()
        modified_input[h] = set_obstacle(modified_input[h], w)
        location = find_guard()
        d = 0
        starting_situation = [location,d]
        distinct_situations = [starting_situation]
        onmap = True
        while onmap:
            new_location = [location[0] + directions[d][0], location[1] + directions[d][1]]
            if not (new_location[0] >= 0 and new_location[0] < map_width and new_location[1] >= 0 and new_location[1] < map_height):
                onmap = False    
                continue
            new_tile = modified_input[new_location[1]][new_location[0]]
            if new_tile == "." or new_tile == "^":
                #print("moving")
                location = new_location
                situation = [location,d]
                if situation in distinct_situations:
                        onmap = False
                        potential_locations.append([w,h])
                        print(len(potential_locations))
                else:
                    distinct_situations.append(situation)
            if new_tile == "#":
                #print("turn right")
                d = (d+1)%4
            

print(len(potential_locations))