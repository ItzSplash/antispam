import discord, asyncio
from discord.ext import commands

class administration():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True , help= "deletes a large amount of messages",  aliases=["prune"])
    async def purge(self, ctx):
        if ctx.message.author.permissions_in(ctx.message.channel).manage_messages == True:
            split = ctx.message.content.split(" ") 
            if len(split) == 1:
                await self.bot.say("**Must Provide a Number**")
            else:
                deletedmessage =  ctx.message.content.split(" ")[1]
                await self.bot.purge_from(ctx.message.channel , limit = int(deletedmessage),  check=None)

        else: await self.bot.say("You don't have the **manage messages** permission!")
    
    @commands.command(pass_context=True , help="kicks a certain user")
    async def kick(self , ctx):
        split = ctx.message.content.split(" ")
        
        if ctx.message.author.permissions_in(ctx.message.channel).kick_members == True:
            split = ctx.message.content.split(" ")
            if len(split) == 1:
                await self.bot.say("**Must Provide a User**")
            else:
                await self.bot.say("Are you sure you want to kick this person? Type `yes or no`.")
                waitmsg = await self.bot.wait_for_message(15, channel=ctx.message.channel, author = ctx.message.author)
                if waitmsg.content.lower() == "no":
                    await self.bot.say("user was not kicked")
                if waitmsg.content.lower() is None:
                    await self.bot.say("user was not kicked")
                if waitmsg.content.lower() == "yes":
                    id = split[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
                    member = ctx.message.server.get_member(id)
                    if(member == None):
                        return await self.bot.say("User not found!")
                    try:
                        await self.bot.kick(member)
                        await self.bot.say("**Kicked** " + member.name)
                    except:
                        return await self.bot.say("**I don't have enough permissions**!!") 
        else:
            await self.bot.say("**You don't have enough permissions to kick someone!**")
    
    @commands.command(pass_context=True, help= "bans a given user")
    async def ban(self , ctx):
        if ctx.message.author.permissions_in(ctx.message.channel).ban_members == True:
            split = ctx.message.content.split(" ") 
            if len(split) == 1:
                await self.bot.say("**Must Provide a User**")
            else:
                await self.bot.say("Are you sure you wanna ban this person? Type `yes or no`.")
                waitmsg = await self.bot.wait_for_message(15, channel=ctx.message.channel, author = ctx.message.author)
                if waitmsg.content.lower() == "no":
                    await self.bot.say("user was not banned")
                if waitmsg.content.lower() is None:
                    await self.bot.say("user was not banned")
                if waitmsg.content.lower() == "yes":
                    id = split[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
                    member = ctx.message.server.get_member(id)
                    if(member == None):
                        return await self.bot.say("User not found!")
                    try:
                        await self.bot.ban(member , delete_message_days=1)
                        await self.bot.say(member.name + " *Got the* **BAN HAMMER**")
                    except:
                        return await self.bot.say("*I don't have permissions!!*") 
        else:
            await self.bot.say("*You don't have enough permissions to ban someone!*")

    @commands.command(pass_context = True , help = "mutes user mentioned")
    async def mute(self , ctx , member:discord.Member):
        if ctx.message.author.permissions_in(ctx.message.channel).manage_roles == True:
            muted_role = discord.utils.get(ctx.message.server.roles, name = "Muted")
            await self.bot.add_roles(member , muted_role)
            await self.bot.say("muted " + member)
        else: await self.bot.say("You must have the `manage_roles` permission")
    @commands.command(pass_context = True , help = "unmutes user mentioned")
    async def unmute(self , ctx , member:discord.Member):
        if ctx.message.author.permissions_in(ctx.message.channel).manage_roles == True:
            muted_role = discord.utils.get(ctx.message.server.roles, name = "Muted")
            await self.bot.remove_roles(member , muted_role)
            await seld.bot.say("unmuted" + member)

        else: await self.bot.say("You must have the `manage_roles` permission")

    @commands.command(pass_context= True , help = "gives you a role")
    async def iam(self, ctx):
        role_name = ctx.message.content[5:].lower()
        for role in ctx.message.server.roles:
            if role.name.lower() == role_name:
                await self.bot.add_roles(ctx.message.author , role)
                await self.bot.send_message(ctx.message.channel , "added the **" + ctx.message.content[5:] + "** role!")

    @commands.command(pass_context= True , help = "takes away a role")
    async def imnot(self , ctx):
        role_name = ctx.message.content[7:]
        for role in ctx.message.server.roles:
            if role.name.lower() == role_name:
                    await self.bot.remove_roles(ctx.message.author , role)

    @commands.command(pass_context= True)
    @commands.has_permissions(manage_roles=True)
    async def makerole(self , ctx, *, name):
        '''Creates a role'''
        await self.bot.create_role(ctx.message.server , name=name)



def setup(bot):
    bot.add_cog(administration(bot))