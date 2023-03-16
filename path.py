# Computes the distances of paths through cities.
# CSC 101, Project 5
# Given code, Winter '23
# TODO: Complete this file.
import sys

def main():
    filename = sys.argv[1]
    with open(filename, "r") as file:
       lst = []
       for line in file:
           stripped = line.strip()
           eachLine = stripped.split(",")
           lst.append(eachLine)  
 
    keys = lst.pop(0)
    lis = []
    cities = [] 

    for i in range(len(lst)):
        lst[i][2] = int(lst[i][2])

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if type(lst[i][j]) == str and lst[i][j] not in cities:
                cities.append(lst[i][j])
    cities = sorted(cities)

    for items in lst:
        lis.append([(i) for i in items])

    d = []
    for items in lis:
        d.append(dict(zip(keys,(items))))   

    print("The options are:")
    city = {}
    for i in range(len(cities)):
        city[i] = cities[i]
        print("    " + str(i) + ": " + city[i])
    key = int(input("Where to start? \n"))
    home = city[key] 
    distance = 0
    temp = city
   
    end = ""
    while end != home:
        start = temp[key]
        print("Welcome to " + start + "!")
        print("The options are:")
        temp = []
        for item in d:
            if item["Start"] == start: 
                temp.append(item["End"])
        temp = sorted(temp)

        for i in range(len(temp)):
            print("    " + str(i) + ": " + temp[i])

        key = int(input("Where to next? \n"))
        end = temp[key]
        for item in d:
            if item["Start"] == start and item["End"] == end:
                distance += item["Distance"]  
    print("Welcome home! Your total distance traveled is " + str(distance) + ".") 

if __name__ == "__main__":
    main()
