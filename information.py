import discord, asyncio
from discord.ext import commands

class information():
    def __init__(self, bot):
        self.bot = bot
	

    @commands.command(pass_context=True , help = "?nickname (name), changes nickname, ?nickname to go back to normal")
    async def nickname(self , ctx):
        await self.bot.change_nickname(ctx.message.author , ctx.message.content[10:])
        await self.bot.send_message(ctx.message.channel ,"You changed ur nickname to **" + ctx.message.content[10:] + "**")
 

    @commands.command(pass_context = True , help = "shows your / someone elses avatar")
    async def avatar(self , ctx):
        if len(ctx.message.content.split(" ")) == 1:
            await self.bot.say(ctx.message.author.avatar_url.replace("?size=1024" , ""))
        else:
            id = ctx.message.content.split(" ")[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
            member = ctx.message.server.get_member(id)
            await self.bot.say(member.avatar_url.replace("?size=1024" , ""))

    @commands.command(pass_context = True)
    async def userid(self , ctx):
        if len(ctx.message.content.split(" ")) == 1:
            await self.bot.say(ctx.message.author.mention + ", your userID is **" + ctx.message.author.id + "**")
        else:
            id = ctx.message.content.split(" ")[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
            member = ctx.message.server.get_member(id)
            await self.bot.say("The person's userID is **" + member.id + "**")


    @commands.command(pass_context = True)
    async def userinfo(self , ctx):
        if len(ctx.message.content.split(" ")) == 1:
            await self.bot.say("```" + ctx.message.author.name + ", Your discriminator is " + ctx.message.author.discriminator + "```")
        else:
            id = ctx.message.content.split(" ")[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
            member = ctx.message.server.get_member(id)
            await self.bot.say("```The person's discrim is " + member.discriminator + "```")
    @commands.command(pass_context = True, help = "creates an invite for one use, for 24 hours")
    async def serverinvite(self , ctx):
        try: 
            serverinvite = await self.bot.create_invite(ctx.message.server , max_age = 86400 , max_uses = 1)
            await self.bot.send_typing(ctx.message.channel)
            await asyncio.sleep(5)
            await self.bot.say(serverinvite)
        except discord.Forbidden:
            await self.bot.say("i dont have the `create instant invite` permission!")
        
    @commands.command()
    async def invite(self):
        return await self.bot.say('You can invite my bot to your server with this link:<https://discordapp.com/api/oauth2/authorize?client_id=332647811885694987&scope=bot&permissions=335670422> \n to use the administration commands, you must keep the permissions the same.')

        

		
def setup(bot):
    bot.add_cog(information(bot))