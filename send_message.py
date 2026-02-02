#Written by CJ Freimund for UW-Whitewater's Association for Computing Machinery
import os
from dotenv import load_dotenv
import datetime
from genProblem import generateProblem

import discord
from discord.ext import commands,tasks

load_dotenv()
token = os.getenv("TOKEN","")
channelID = int(os.getenv("ACMCHANNEL",""))
roleID = int(os.getenv("ACMROLE",""))

intents = discord.Intents.default()
intents.guilds = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged onto discord as {bot.user.name}")
    channel = bot.get_channel(channelID)
    guild = channel.guild
    role = discord.Guild.get_role(guild,roleID)
    
    print(f"Sending problem message to {channel.name}, pinging role {role}")
    if not sendfilewithmessage.is_running():
        sendfilewithmessage.start()


@tasks.loop(minutes=1)
async def sendfilewithmessage():
    """Sends a file with a weekly problem, will attach a file if the problem generated is from ICPC."""
    DAY = datetime.date.today().weekday()
    TIME = datetime.datetime.now()
    guild = bot.get_channel(channelID).guild
    role = discord.Guild.get_role(guild,roleID)
    #if(True):
    if(DAY == 0 and TIME.hour == 12 and TIME.minute == 0):
        mess = generateProblem()
        file_path = mess[1]
        message_content = f"Happy Monday <@&{role.id}>!"
        message_content += mess[0]
        channel = bot.get_channel(channelID)

        try:
            with open(file_path, 'rb') as f:
                discord_file = discord.File(f, filename='WeeklyProblem.pdf')
                await channel.send(content=message_content, file=discord_file)
        except FileNotFoundError:
            print(f"{DAY}: No file needed!")
            await channel.send(content=message_content)
        except Exception as e:
            await channel.send(f"An error occurred: {e}")

bot.run(token)