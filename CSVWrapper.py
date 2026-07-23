import csv
from LeetCodePlug.leetcodeplug import has_user_solved


FILE = "Data/playerdata.csv"

def searchPlayer(user):
    """Searches for a user from the playerlist"""
    with open(FILE,'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if user in row:
                return 1
        return 0

def addPlayer(user):
    """Adds a user from the playerlist"""
    if not searchPlayer(user):
        with open(FILE,'a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([user,0])
    pass

def removePlayer(user):
    """Removes a user from the playerlist"""
    updated_rows = []
    found = False
    with open(FILE, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row and row[0] == user:
                found = True
                continue
            updated_rows.append(row)
    if found:
        with open(FILE, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(updated_rows)
            return 1
    return 0

def getUserList():
    """Returns a list of player usernames and scores"""
    with open(FILE, 'r',newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = []
        for row in reader:
            data.append([row[0],int(row[1])])
        return data

def scorecheck(problem):
    data = getUserList()
    for x in data:
        if has_user_solved(x[0],problem) == 1:
            x[1] = str(int(x[1]) + 50)
    with open(FILE, 'w',newline='') as csvfile:
        for x in data:
            csvfile.write(f"{x[0]},{x[1]}\n")
