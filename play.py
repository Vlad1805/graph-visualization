#!/usr/bin/python3
# Copyright 2021 Butnariu Bogdan-Mihai

# libraries
import os

# variables

# variables for bash commands
clear = "clear"
chmod = "chmod +x src/"
pip3 = "sudo apt-get install python3-pip && echo pip3 passed. || echo pip3 failed."
networkx = "pip3 install networkx && echo Networkx passed. || echo Networkx failed."
matplotlib = "pip3 install matplotlib && echo Matplotlib passed. || echo Matplotlib failed."
   
# dictionary for algorithms
algo = {
    '1' : 'BFS',
    '2' : 'DFS',
    '3' : 'Dijkstra',
    '4' : 'Floyd_Warshall'
}

def load_message(string, n): # function that adds n '.' after mes, used for loading screens
    dots = "."
    for i in range(n):
        print(string + dots) # first step, the message and one dot
        os.system("sleep 0.5")
        
        dots += '.' # growth of dots
        
        if i == n-1:
            continue
        
        os.system(clear)

def entry(): # function that reads the input for matrix
    n = int(input("Enter the number 'n' for n*n adjacency matrix: "))
        
    matrix = []
    for i in range(n):
        print(f"Enter the {i+1} row, {n} numbers are expected in a single row:")
            
        string = input()
        elements = list(string.split(" "))
        elements = [i for i in elements if i.isnumeric()] # create a list with numbers only
            
        while len(elements) < n or len(elements) > n: # condition for input, a row,  to contain 'n' numbers
            print("Wrong input. Try again: ")
            string = input()
            elements = list(string.split(" "))
            elements = [i for i in elements if i.isnumeric()] 
        matrix.append(elements)
        
    root = int(input("Enter the starting root: "))
    return matrix, n, root

def input_file(matrix, n, root): # function that writes the input on file
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

def input_print(matrix, n, root): # function that writes the input on screen
    print("\nYour input was,")
    print('Adjacency Matrix:')    
    for i in range(n):
        print("   ", end='')
        for j in range(n):
            if j == n - 1:
                print(f"{matrix[i][j]}")
            else:
                print(f"{matrix[i][j]}", end=" ")
    print(f"Starting root: {root}")

# clearing the terminal
os.system(clear)

# permissions for the algoritmhs
for key in algo.keys():
    os.system(chmod + f"/{algo[key]}/{algo[key]}.py")

# 1st choice screen, yes or quit
load_message("Welcome to Graph Visualization Tool! Press 'y' to continue or 'q' to exit", 5)
response = input()
while True: 
    if response == 'y':
        break
    elif response == 'q':
        print("Bye!")
        exit()
        break
    else:
        response = input("Wrong button!\n")

# 2nd choice screen, yes or no
response = input("Do you have all the needed packeges already installed? [y/n]: ")
while True:
    if response == 'y':
        break
    elif response == 'n':
        os.system(pip3) # install python3-pip
        os.system(networkx) # "---"
        os.system(matplotlib) # "---"
        break    
    else:
        response = input("Wrong button!\n")

# 3rd choice screen, algorithm choice
choice = input("Select an algorithm for the graph:\n\t1: BFS\n\t2: DFS\n\t3: Dijkstra\n\t4: Floyd Warsahll\nChoice: ")
while True:
    if choice.isnumeric():
        
        if int(choice) > 0 and int(choice) < 5:
            print(f"Your choice is {algo[choice]} algorithm. Please select to entry input, show example or retry. [i/e/r]: ", end="") # 4th choice
            response = input()            
            
            if response == 'r':
                choice = input("Choice: ") # retry 3rd choice
                continue
            else:
                break

        else:
            choice = input("Not a valid choice! Retry: ")

    else:
        choice = input("Not a number! Retry: ")

# construction of input.txt, based on choices
while True:
    if response == 'e': # example choice
        if choice == '1':
            n = 5
            matrix = [
                ['0', '5', '10', '5', '0'],
                ['0', '0', '5', '0', '12'],
                ['0', '10', '0', '0', '3'],
                ['0', '0', '10', '0', '0'],
                ['0', '0', '0', '0', '0']
            ]
            root = 0
            
            load_message("Loading", 6)
            print("Done! Now you have a graph!")
            input_file(matrix, n, root)
            input_print(matrix, n, root)
        
        elif choice == '2':
            n = 6
            matrix = [
                ['0', '1', '0', '0', '0', '1'],
                ['0', '0', '0', '1', '0', '0'],
                ['1', '0', '0', '0', '0', '0'],
                ['0', '0', '1', '0', '1', '0'],
                ['0', '0', '0', '1', '0', '0'],
                ['0', '0', '0', '0', '0', '0']
            ]
            root = 0
            
            load_message("Loading", 6)
            print("Done! Now you have a graph!")
            input_file(matrix, n, root)
            input_print(matrix, n, root)
        
        elif choice == '3':
            n = 5
            matrix = [
                ['0', '2', '7', '-1', '-1'],
                ['-1', '0', '3', '8', '5'],
                ['-1', '2', '0', '0', '-1'],
                ['-1', '-1', '-1', '0', '4'],
                ['-1', '-1', '-1', '5', '0']
            ]
            root = 2
            
            load_message("Loading", 6)
            print("Done! Now you have a graph!")
            input_file(matrix, n, root)
            input_print(matrix, n, root)
        break

    elif response == 'i': # input choice
        matrix, n, root = entry()
        load_message("Loading", 6)
        print("Done! Now you have a graph!")
        input_file(matrix, n, root)
        input_print(matrix, n, root)
        break

    else: # exit choice
        response = input("Not a valid choice! Retry or exit [q]: ")
        if response == 'q':
            print("Bye!")
            exit()

# command that executes the chosen algorithm
os.system(f"./src/{algo[choice]}/{algo[choice]}.py")