#!/usr/bin/python3
# Copyright 2021 Butnariu Bogdan-Mihai

# libraries
import os
import time

def load_message(mes, n): # function that add n '.' after mes, used for loading screens
    dots = "."
    for i in range(n):
        print(mes + dots)
        time.sleep(0.5)
        dots += '.'
        if i < n-1:
            os.system(clear)
        else:
            continue

# variables
   # variables for bash commands
clear = "clear"
networkx = "pip3 install networkx >> /dev/null && echo Networkx passed. || echo Networkx failed."
matplotlib = "pip3 install matplotlib >> /dev/null && echo Matplotlib passed. || echo Matplotlib failed."
   # variables for screens
intro = "Welcome to Graph Visualization Tool! Press 'y' to continue or 'q' to exit"
ques1 = "Do you have installed all the packages needed? [y/n]: "
ques2 = "Select an algorithm for the graph:\n\t1: BFS\n\t2: DFS\n\t3: Dijkstra\n\t4: Floyd Warsahll\nChoice: "
   # variables for input.txt
root = int()
n = int()
   # dictionary for algorithms
algo = {
    '1' : 'BFS',
    '2' : 'DFS',
    '3' : 'Dijkstra',
    '4' : 'Floyd_Warshall'
}

# loading screen
os.system(clear)
load_message(intro, 5)

# 1# choice screen
response = input()
while True: 
    if response == 'y':
        break
    elif response == 'q':
        print("Bye!")
        exit()
        break
    else:
        print("Wrong button!")
        response = input()


response = input(ques1)
while True:
    if response == 'y':
        break
    elif response == 'n':
        os.system(networkx)
        os.system(matplotlib)
        break    
    else:
        print("Wrong button!")
        response = input()

choice = input(ques2)
while True:
    if choice.isnumeric():
        
        if int(choice) > 0 and int(choice) < 5:
            print(f"Your choice is {algo[choice]} algorithm. Please select to entry input, show example or retry. [i/e/r]: ", end="")
            response = input()            
            
            if response == 'r':
                choice = input("Choice: ")
                continue
            else:
                break

        else:
            choice = input("Not a valid choice! Retry: ")        
    else:
        choice = input("Not a number! Retry: ")

while True:
    if response == 'e':
        break

    elif response == 'i':
       
        n = int(input("Enter the number 'n' for n*n matrix: "))
        
        matrix = []
        for i in range(n):
            print(f"Enter the {i+1} row, {n} numbers are expected:")
            
            string = input()
            elements = list(string.split(" "))
            elements = [i for i in elements if i.isnumeric()] 
            
            while len(elements) < n or len(elements) > n:
                print("Gresit.")
                string = input()
                elements = list(string.split(" "))
                elements = [i for i in l if i.isnumeric()]  
            matrix.append(l)
        
        root = int(input("Enter the starting root: "))
        
        out = open("input.txt", "w")
        out.write(f"{n}\n")
        
        for i in range(n):
            for j in range(n):
                if j == n - 1:
                    out.write(f"{matrix[i][j]}\n")
                else:
                    out.write(f"{matrix[i][j]} ")
        
        out.write(f"{root}")
        out.close()
        break

    else:
        response = input("Not a valid choice! Retry or exit [q]: ")
        if response == 'q':
            print("Bye!")
            exit()

load_message("Loading", 6)
os.system(f"./src/{algo[choice]}/{algo[choice]}.py")
print("Done! Now you have a graph!")

if response == 'i':
    print("\nYour input was:")
    print(f"n: {n}")
    print('matrix:')    
    for i in range(n):
        for j in range(n):
            if j == n - 1:
                print(f"{matrix[i][j]}")
            else:
                print(f"{matrix[i][j]}", end=" ")
    print(f"Starting root: {root}")
