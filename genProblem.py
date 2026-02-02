import random
import pandas as pd

def generateProblem():
    """Pulls a random problem from Leetcode, Advent of Code, or an ICPC World Finals.

    Returns:
        set[str]: [message,filepath]
        
        message: A message for the Discord Bot to post in chat.
        
        filepath: If an ICPC problem is chosen, this is the PDF filepath, Otherwise returns "".
    """
    message = "\nThis week's problem is "
    filepath = ""
    provider=random.randint(0,2)
    if(provider==0): #Leetcode
        df = pd.read_csv('lc-dataset.csv')
        problem = random.randint(0,1428)
        message+=f"a {df['difficulty'][problem]} problem from Leetcode!\nThe problem chosen is **Problem {df['id'][problem]}: {df['title'][problem]}**\nHere is a Link: {df['url'][problem]}"
    if(provider==1): #Advent of Code
        year = random.randint(2015,2024)
        day = random.randint(1,25)
        message+=f"day {day} of the {year} Advent of Code!\nHere is a Link: https://adventofcode.com/{year}/day/{day}"
    if(provider==2): #ICPC
        year = 2025#random.randint(2013,2025)
        df = pd.read_csv(f'Problems/{year}/{year}ICPC.csv')
        problem = random.randint(0, int(df.size/2))
        message+=f"{df['title'][problem]} from the {year} ICPC World Finals!\nA PDF is attached!"
        filepath+=f"Problems/{year}/{df['id'][problem]}-{df['title'][problem]}.pdf"
    message+="\nGood Luck!"

    A = []
    A.append(message)
    A.append(filepath)
    return A