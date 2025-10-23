#Written by CJ Freimund for UW-Whitewater's Association for Computing Machinery
import os
from dotenv import load_dotenv
import datetime

import discord
from discord.ext import commands,tasks

load_dotenv()
token = os.getenv("TOKEN","")
channelID = int(os.getenv("CHANNEL",""))


intents = discord.Intents.default()
intents.guilds = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged onto discord as {bot.user.name}")
    if not sendfilewithmessage.is_running():
        sendfilewithmessage.start()
        #send_periodic_message.start()

@tasks.loop(minutes=5)
async def sendfilewithmessage():
    """Sends a file with a message."""
    file_path = 'Problems/2024A.pdf'  # Replace with the actual path to your file
    message_content = "Here's the file you requested!"
    channel = bot.get_channel(channelID)

    try:
        with open(file_path, 'rb') as f:
            discord_file = discord.File(f, filename='WeeklyProblem.pdf') # You can specify a different filename for Discord
            await channel.send(content=message_content, file=discord_file)
    except FileNotFoundError:
        await channel.send(f"Error: File not found at {file_path}")
    except Exception as e:
        await channel.send(f"An error occurred: {e}")

# async def send_periodic_message():
#     channel = bot.get_channel(channelID)
#     if channel:
#         await channel.send(content="This is a periodic message!", file="Problems/2024A.pdf")
#     else:
#         print(f"Channel with ID {channelID} not found.")

bot.run(token)