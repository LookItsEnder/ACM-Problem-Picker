import os
# import discord
from  LeetCodePlug.leetcodeplug import has_user_solved

def addPlayer(name):
    FILE = "Data/playerdata.txt"
    # tmp=open(FILE,'w')
    # tmp.close
    with open(FILE,'r') as data:
        content = data.read()
        if name in content:
            return 0

    with open(FILE, "a") as data:
        data.write(name + "\n")

    return 1

def getPlayerList():
    FILE = "Data/playerdata.txt"
    


name = input("Enter a Username: ")
if(addPlayer(name)):
    print("Successfully added user!")
else:
    print("ERROR: Internal Error!")
    exit(1)

# user = "Look_Its_Ender"          # Replace with target username
problem = "two-sum"         # Replace with target problem slug
solved = has_user_solved(name, problem)

if solved == 1:
    print(f"{name} has solved '{problem}' recently!")
else:
    match solved:
        case 0:
            print(f"{name} has not solved '{problem}' yet!")
        case 1:
            print(f"{name} has solved '{problem}' recently!")
        case -1:
            print(f"No recent submissions found or user '{name}' does not exist.")
        case -2:
            exit(-2)