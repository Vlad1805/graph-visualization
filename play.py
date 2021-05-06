#!/bin/python3
# Copyright 2021 Butnariu Bogdan-Mihai

import os
import time

def load_message(mes, n):
    dots = "."
    for i in range(n):
        print(mes + dots)
        time.sleep(0.5)
        dots += '.'
        if i < n-1:
            os.system(clear)
        else:
            continue

sleep = "sleep 10"
clear = "clear"

networkx = "pip3 install neworkx >> /dev/null && echo Networkx passed. || echo Networkx failed."
matplotlib = "pip3 install matplotlib >> /dev/null && echo Matplotlib passed. || echo Matplotlib failed."

bfs = "./src/BFS/BFS.py"
dfs = "./src/DFS/DFS.py"
dij = "./src/Dijkstra/Dijkstra.py"
flo = "./src/Floyd_Warshall/Floyd_Warshall.py"

intro = "Welcome to Graph Visualization Tool! Press 'y' to continue or 'q' to exit"
ques1 = "Do you have installed all the packages needed? [y/n]: "
ques2 = "Select an algorithm for the graph:\n\t1: BFS\n\t2: DFS\n\t3: Dijkstra\n\t4: Floyd Warsahll\nChoice: "

root = int()
n = int()

algo = {
    '1' : 'BFS',
    '2' : 'DFS',
    '3' : 'Dijkstra',
    '4' : 'Floyd_Warshall'
}

os.system(clear)

load_message(intro, 5)

response = input()
while True:
    if response == 'q':
        print("Bye!")
        exit()
        break
    elif response == 'y':
        break
    else:
        print("Wrong button!")
        response = input()

print(ques1, end='')
response = input()
while True:
    if response == 'y' or response == 'n':
        break
    else:
        print("Wrong button!")
        response = input()

if response == 'n':
    os.system(networkx)
    os.system(matplotlib)

choice = input(ques2)
while True:
    if choice.isnumeric():
        
        if int(choice) > 0 and int(choice) < 5:
            print(f"Your choice is {algo[choice]} algorithm. Please select to entry input, show example or retry. [i/e/r]: ", end="")
            response = input()            
            
            if response == 'r':
                print(ques2)
                choice = input(ques2)
                continue
            else:
                break
        else:
            choice = input("Not a valid choice! Retry: ")        
    else:
        choice = input("Not a number! Retry: ")

while True:
    if response == 'i':
       
        n = int(input("Enter the number 'n' for n*n matrix: "))
        matrix = []
        for i in range(n):
            print(f"Enter the {i+1} row, with space between numbers:")
            matrix.append(input())
        
        root = int(input("Enter the starting root: "))
        
        out = open("input.txt", "w")
        out.write(f"{n}\n")
        
        for i in range(n):
            out.write(f"{matrix[i]}\n")
        
        out.write(f"{root}")
        out.close()
        break
    
    elif response == 'e':
        break
    
    else:
        response = input("Not a valid choice! Retry or exit [q]: ")
        if response == 'q':
            print("Bye!")
            exit()

load_message("Loading", 6)

print("Done! Now you have a graph!")

os.system(f"./src/{algo[choice]}/{algo[choice]}.py")

if response == 'i':
    print("\nYour input was:")
    print(f"n: {n}")
    print('matrix:')
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = " ")
        print()
    print(f"Starting root: {root}")
    
