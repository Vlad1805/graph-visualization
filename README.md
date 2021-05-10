# graph-visualization

Graph visualization tool using python3 networkx module for linux.
Run play.py script to open the program or run each file individually to generate the output.

# play.py script

This script runs all the algorithms that we propouse for this project. Is using Pythonn languange and
a few bash commands for the installation of pyhton-pip3, networkx and matplotlib.

⬤ How it's made:
In the file, you'll see 4 functions:

~def loading_message(string, n)
    This displays the 'string' message followed by 'n' dots using 'clear' and 'sleep' from bash

~def entry()
    This is formating the user input for the input.txt file. Makes a list only with numbers and append it 
    in the 'matrix' list.

~def input_file(matrix, n, root)
    This open a file in 'write' mode and writes the dimension of matrix 'n', the 'matrix' and the starting root.

~def input_print(matrix, n, root)
    This prints the user input on the terminal.

In total, they're are x choices:

              --- yes
1st choice ---|   or
              --- quit
    Used for the first question.


              --- yes
2nd choice ---|   or
              --- no
    Used for the second question, if the user has all the needed packages.
             

                  --- 1 -> BFS
              |---|
              |   --- 2 -> DFS
3rd choice ---|   
              |   --- 3 -> Dijkstra
              |---| 
                  --- 4 -> Floyd Warshall
    Used for the third question, when the user select the algorithm.

              |--- input
              |
4th choice ---|--- example
              |
              |--- retry
    Used for the forth question. Is generating the adjacency matrix. It can be with the user input,
    one example for each algorithm or you can retry the selection of the algorithm (retry 3rd choice).

In the final part, the script runs the algorithm.py file and a window with the choosen graph in showing.

# Copyright 2021

Butnariu Bogdan-Mihai,
Podaru Andrei-Alexandru,
Popescu Silviu,
Stanciu Vlad
