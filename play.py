#!/bin/python3
# Copyright 2021 Butnariu Bogdan-Mihai

import os
import time

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
dots = "."

algo = {
    '1' : 'BFS',
    '2' : 'DFS',
    '3' : 'Dijkstra',
    '4' : 'Floyd_Warshall'
}

os.system(clear)

for i in range(5):
    print(intro + dots)
    time.sleep(0.5)
    dots += '.'
    if i < 4:
        os.system(clear)
    else:
        continue

response = input()
while True:
    if response == 'q':
        print("Bye!")
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
            print(f"Your choice is {algo[choice]} algorithm. Please select to entry input or show example. [i/e]: ")
            break
        else:
            choice = input("Not a valid choice! Retry: ")        
    else:
        choice = input("Not a number! Retry: ")

response = input()
while True:
    if response == 'i':
        pass
        break
    elif response == 'e':
        os.system(f"./src/{algo[choice]}/{algo[choice]}.py")
        break
    else:
        response = input("Not a valid choice! Retry or exit [q]: ")
        if response == 'q':
            print("Bye!")
            exit()
print("Done!")
    
