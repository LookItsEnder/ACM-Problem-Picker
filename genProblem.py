import random
import pandas as pd

lcName=[]
lcDiff=[]
lcURL=[]

#print(df.head()) # Display the first few rows


def generateProblem():
    message = "This week's problem is "
    provider=1#random.randint(0,2)
    if(provider==0): #Leetcode
        df = pd.read_csv('lc-dataset.csv')
        problem = random.randint(0,1428)
        message+=f"a {df['difficulty'][problem]} problem from Leetcode!\nThe problem chosen is **Problem {df['id'][problem]}: {df['title'][problem]}**\n Link: {df['url'][problem]}"
    if(provider==1): #Advent of Code
        year = random.randint(2015,2024)
        day = random.randint(1,25)
        message+=f"day {day} of the {year} Advent of Code!\nLink: adventofcode.com/{year}/day/{day}"
    if(provider==2): #ICPC
        year = random.randint(2013,2025)
        message+=f"from the {year} ICPC World Finals!\nA PDF is attached!"

    print(message)


generateProblem()