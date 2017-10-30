import discord
import os
import time
import discord
import random
import asyncio
from discord.ext import commands

#you can change the prefix to what you want, just keep it inside the quotations
bot =commands.Bot(command_prefix ="!")

@bot.event
async def on_ready():
    #what the terminal say when the bot goes online
    print("Anti-Spam Bot is Online!, running version " + discord.__version__ + " of Discord.py")
    await asyncio.sleep(10)
    #this sets what tame the bot is playing
    await bot.change_presence(game=discord.Game(name="https://github.com/ItzSplash/antispam", type=1))

@bot.command()
async def ping():
    await bot.say("pong!")
    
@bot.event
async def on_message(message):
    if message.context.startswith("!spam"):
        if 
   

    #insert your bot token here inside the quotations
bot.run("bot token")
