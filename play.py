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
                choice = input("Retry your choice for algorithm: ")
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
            print(f"Enter the {i+1} row, {n} numbers are expected:")
            
            string = input()
            l = list(string.split(" "))
            l = [i for i in l if i.isnumeric()] 
            
            while len(l) < n or len(l) > n:
                print("Gresit.")
                string = input()
                l = list(string.split(" "))
                l = [i for i in l if i.isnumeric()]  
            matrix.append(l)
        print(matrix)
        
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

        load_message("Loading", 6)
        print("Done! Now you have a graph!")

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

        break
    
    elif response == 'e':
        load_message("Loading", 6)
        print("Done! Now you have a graph!")
        break

    else:
        response = input("Not a valid choice! Retry or exit [q]: ")
        if response == 'q':
            print("Bye!")
            exit()

os.system(f"./src/{algo[choice]}/{algo[choice]}.py")