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
    
@bot.command(pass_context = True)
async def spam(ctx)
    if ctx.message.author.permissions_in(ctx.message.channel).manage_server== True:
        await bot.say("This channel is now closed - if you message this channel and you dont have a role, you will  be muted")
        waitmsg = await self.bot.wait_for_message(channel=ctx.message.channel, author = ctx.message.author)
        async def on_message(message):
            #do shit about muting people
            #do a wait_for_message
        if waitmsg.content.lower() == "!spam stop":
            return
            
        
        
    
            
   

    #insert your bot token here inside the quotations
bot.run("bot token")
