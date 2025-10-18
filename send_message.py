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
    if not send_periodic_message.is_running():
        send_periodic_message.start()

@tasks.loop(minutes=5)
async def send_periodic_message():
    channel = bot.get_channel(channelID)
    if channel:
        await channel.send("This is a periodic message!")
    else:
        print(f"Channel with ID {channelID} not found.")

bot.run(token)