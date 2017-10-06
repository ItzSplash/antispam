import discord, asyncio
from discord.ext import commands
import random

class fun():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True , help = "?say (text) bot says what u typed")
    async def say(self , ctx):
        await self.bot.say(ctx.message.content[5:])
        await self.bot.delete_message(ctx.message)

    @commands.command(pass_context= True)
    async def add(self, ctx):
        """Adds two numbers together."""
        left = int(ctx.message.content.replace("+" , " ").replace("   " , " ").split(" ")[1])
        right = int(ctx.message.content.replace("+" , " ").replace("   " , " ").split(" ")[2])
        await self.bot.say(left + right)
        
    @commands.command(pass_context= True)
    async def subtract(self, ctx, aliases = "minus"):
        """subtracts two numbers together."""
        left = int(ctx.message.content.replace("-" , " ").replace("   " , " ").split(" ")[1])
        right = int(ctx.message.content.replace("-" , " ").replace("   " , " ").split(" ")[2])
        if right > left:
            await self.bot.say("**cannot do negative numbers**")
        else: await self.bot.say(left - right)

    @commands.command(pass_context= True)
    async def divide(self, ctx, alias = "div"):
        """divides two numbers together."""
        left = int(ctx.message.content.replace("/" , " ").replace("   " , " ").split(" ")[1])
        right = int(ctx.message.content.replace("/" , " ").replace("   " , " ").split(" ")[2])
        await self.bot.say(left / right)

    @commands.command(pass_context= True)
    async def multiply(self, ctx, alias= "times"):
        """multiplies two numbers together."""
        left = int(ctx.message.content.replace("*" , " ").replace("   " , " ").split(" ")[1])
        right = int(ctx.message.content.replace("*" , " ").replace("   " , " ").split(" ")[2])
        await self.bot.say(left * right)

    @commands.command(pass_context=True)
    async def suicide(self , ctx):
        await self.bot.send_file(ctx.message.channel , "suicide.png")     

    @commands.command(pass_context=True , help = "types lenny and deletes your message")
    async def lenny(self , ctx):
        await self.bot.say("( ͡° ͜ʖ ͡°)")
        await self.bot.delete_message(ctx.message)

    @commands.command(pass_context= True)
    async def taste(self , ctx):
        await self.bot.say(ctx.message.content[7:] + " has shit taste")
    
    playlists = "weeb" , "chill"
    def check(msg):
        return msg.content.lower() in playlists

    @commands.command(pass_context = True , help = "my youtube playlist")
    async def playlist(self , ctx):
        await self.bot.say("which playlist?\n\n-**weeb**\n-**chill**")
        waitmsg = await self.bot.wait_for_message(15, channel=ctx.message.channel, author = ctx.message.author)
        if waitmsg.content.lower() == "weeb":
            return await self.bot.say("http://www.youtube.com/playlist?list=PLEtcXcxy1h1zlhVhyVbtBN6lU6BnNH9tF")
        if waitmsg.content.lower() == "chill":
            return await self.bot.say("https://www.youtube.com/watch?v=qIN4jQ7TgmY&index=1&list=PLm7pUcK8LQsmU9vmMdkdY_tVVMUaumuMs&t=922s")
        else: return await self.bot.say("no playlist was given")
        
    @commands.command(pass_context=True , help = "trump makes it illegal")
    async def illegal(self , ctx):
        if len(ctx.message.content.split(" ")) == 1:
            await self.bot.say("you must include an argument such as `?illegal <text>`")
        else:
            await self.bot.say("https://storage.googleapis.com/is-now-illegal.appspot.com/gifs/" + ctx.message.content[9:].upper().replace(" ", "%20") + ".gif")


    @commands.command(pass_context=True, help= 'picks a random number between 1 and a given number')
    async def roll(self , ctx):
        var = ctx.message.content.split(" ")
        if len(var)==1:
            await self.bot.say("**" + ctx.message.author.name + "**, you rolled a **" + str(random.randint(1,int(var[1]))) + "**!")
        elif len(var)>=2:
            if var[1].isdigit()==False:
                return await self.bot.say('**only positive integers may be used**')
        await self.bot.say("**" + ctx.message.author.name + "**, you rolled a **" + str(random.randint(1,int(var[1]))) + "**!")

    @commands.command(pass_context =True,help ="shows your MAL list, type ?mal (mal username)")
    async def mal(self , ctx):
        await self.bot.say("https://myanimelist.net/animelist/" + ctx.message.content[5:])



def setup(bot):
    bot.add_cog(fun(bot))