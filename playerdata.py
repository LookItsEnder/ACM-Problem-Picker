import os
# import discord
from  APITest.leetcodetest import has_user_solved

def addPlayer(name):
    FILE = "Data/playerdata.txt"
    tmp=open(FILE,'w')
    tmp.close
    with open(FILE,'r') as data:
        content = data.read()
        if name in content:
            return 0
    data.close
    with open(FILE, "w") as data:
        data.write(name)
    data.close
    return 1

name = input("Enter a Username: ")
if(addPlayer(name)):
    print("Successfully added user!")
else:
    print("ERROR: Internal Error!")
    exit(1)

# user = "Look_Its_Ender"          # Replace with target username
problem = "total-waviness-of-numbers-in-range-i"         # Replace with target problem slug
solved = has_user_solved(name, problem)

if solved:
    print(f"{name} has solved '{problem}' recently!")
else:
    print(f"{name} has not solved '{problem}' yet!")