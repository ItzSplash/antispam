import discord
import os
import time
import discord
import random
import asyncio
from discord.ext import commands

bot =commands.Bot(command_prefix ="!")

@bot.event
async def on_ready():
    print("Anti-Spam Bot is Online!, running version " + discord.__version__ + " of Discord.py")
    await asyncio.sleep(10)
    await bot.change_presence(game=discord.Game(name="https://github.com/ItzSplash/antispam", type=1))

@bot.command()
async def ping():
    await bot.say("pong!")

bot.run("bot token")