#!/bin/bash
dots='.'
yes='y'
no='n'
clear

function waiting() {
    for x in $(seq 0 2)
    do
        echo -ne "$1$dots\r"
        sleep 0.3
        dots+='.'
    done
    dots='.'    
}

waiting "Welcome to the Graph-Visualization Tool! Press 'y' to continue or 'n' to exit"

echo
while read input
do
    if [ $input == $yes ]
    then
        break
    elif [ $input == $no ]
    then
        echo "Bye!"
        exit 0
    else
        echo "Wrong button!"
    fi
done
    
echo Do you have installed all the packages needed? [y/n]
read input

if [ $input == $yes ]
then
    echo Great!

else
    waiting 'Please wait'
    sleep 3
    
    if pip3 list | grep networkx >> /dev/null && pip3 list | grep matplotlib >> /dev/null 
    then
        echo Everything is up to date!
    else
        echo -ne "Please be patience while we install what you need.\n"
        sudo pip3 install networkx
        sudo pip3 install matplotlib
        clear
        echo -ne "Everything is up running!"
    fi
fi

