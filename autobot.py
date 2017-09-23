import os
import time
import json
import discord
from discord.ext.commands import Bot
import random
import asyncio
import operator
from discord.ext import commands

Autobot =Bot(command_prefix ="?" , pm_help=True)
@Autobot.event
async def on_ready():
    print("Autobot is Online!, running version " + discord.__version__ + " of Discord.py")
    await asyncio.sleep(10)
    await Autobot.change_presence(game=discord.Game(name="Type ?help", type=1))

@Autobot.command(pass_context=True , help= 'to test if the bot is online')
async def test(ctx):
    print("?test command has been used in " + ctx.message.server.name + " in " + ctx.message.channel.name )
    return await Autobot.say("Autobots, __**Transform and Rollout!**__")

@Autobot.command(pass_context=True , help= "(person) can go kys")
async def kys(ctx):
    print("?kys command has been used" )
    return await Autobot.say(ctx.message.content[5:] + " can go kys")

@Autobot.command(pass_context=True, help= 'shows your MAL, type ?mal (username)')
async def mal(ctx):
    print("?mal command has been used" )
    await Autobot.say("https://myanimelist.net/animelist/" + ctx.message.content[5:])

@Autobot.command()
async def commmands():
    await Autobot.say("use the **?help** command")

EIGHT_BALL_OPTIONS = [" It is certain", "It is decidedly so", "Without a doubt",
                      "Yes definitely", " You may rely on it", " As I see it yes",
                      " Most likely", " Outlook good", " Yes",
                      " Signs point to yes", " Reply hazy try again",
                      "Ask again later", " Better not tell you now",
                      "Cannot predict now", "Concentrate and ask again",
                      "Don't count on it", "My reply is no",
                      "My sources say no", "Outlook not so good",
                      "Very doubtful"]

@Autobot.command(pass_context=True, help= 'shows your prediction')
async def eightball(ctx):
    print("?eightball command has been used" )
    return await Autobot.say('**' + ctx.message.author.name + '**' + " , your prediction :8ball:, **" + random.choice(EIGHT_BALL_OPTIONS) + '**')

@Autobot.command(help= 'invite link for the bot')
async def invite():
    print("?invite command has been used" )
    return await Autobot.say('<https://discordapp.com/api/oauth2/authorize?client_id=332647811885694987&scope=bot&permissions=335670422>')

@Autobot.command(pass_context=True, help= 'rolls a dice')
async def rolldice(ctx):
    print("?rolldice command has been used" )
    rand_roll = ["1" , '2' , '3' , '4' , '5' , '6']
    return await Autobot.say('**' + ctx.message.author.name + '**' + " , your roll is **" + random.choice(rand_roll) + '**' )

Rem_photos = ['http://i.imgur.com/bl9iQsu.jpg' , 'http://i.imgur.com/Nsc5SlA.jpg' , 'http://i.imgur.com/APSU7Bw.jpg' , 'http://i.imgur.com/7wK9PZh.jpg' , 'http://i.imgur.com/EnPQosj.png' , 'http://i.imgur.com/0gr4nkC.jpg' , 'http://i.imgur.com/COqbGN9.jpg' , 'http://i.imgur.com/ASP7BI1.jpg' , 'http://i.imgur.com/dXF1RRG.jpg' , 'http://i.imgur.com/4fOgBsr.jpg' , 'http://i.imgur.com/burcdcN.jpg' , 'http://i.imgur.com/TCCnd8b.jpg' , 'http://i.imgur.com/e6gHCPF.jpg' , 'http://i.imgur.com/bpzTsE2.jpg' , 'http://i.imgur.com/DQJPS8x.jpg' , 'http://i.imgur.com/f7w4RDE.jpg' , 'http://i.imgur.com/yGMqPom.png' , 'http://i.imgur.com/IIG4tpO.jpg' , 'http://i.imgur.com/JQ9U6ix.jpg' , 'http://i.imgur.com/xQU78GY.jpg' , 'http://i.imgur.com/jvmBTXB.jpg' , 'http://i.imgur.com/SUyaU9L.jpg' , 'http://i.imgur.com/gr695hc.jpg' , 'http://i.imgur.com/BVno6l6.png' , 'http://i.imgur.com/Ffn0dyK.jpg' , 'http://i.imgur.com/Gznz3n0.jpg' ,' http://i.imgur.com/WBawS2J.jpg', 'http://i.imgur.com/Mv7fcC9.jpg', 'http://i.imgur.com/kt9YnWG.jpg', 'http://i.imgur.com/iOzFqgh.jpg', 'http://i.imgur.com/hNnO8OX.jpg', 'http://i.imgur.com/YBygo97.jpg', 'http://i.imgur.com/9Iaakhw.jpg', 'http://i.imgur.com/QT1BC8W.jpg', 'http://i.imgur.com/1H7k5m8.jpg', 'http://i.imgur.com/639OCxG.jpg', 'http://i.imgur.com/lz2IXrg.jpg', 'http://i.imgur.com/ZQ6tVyv.png', 'http://i.imgur.com/WZjkDU8.jpg', 'http://i.imgur.com/4GIw1ne.jpg', 'http://i.imgur.com/IoeK3aM.jpg' , 'http://i.imgur.com/HDUeD1F.png', 'http://i.imgur.com/azszJ2B.png', ]

@Autobot.command(pass_context=True, help= 'shows a random pick of Rem from Re:zero')
async def rem():
    print("?rem command has been used" )
    return await Autobot.say(random.choice(Rem_photos))

@Autobot.command(pass_context=True, help= 'picks a random number between 1 and a given number')
async def roll(ctx):
    print("?roll command has been used" )
    var = ctx.message.content.split(" ")
    if len(var)==1:
        await Autobot.say("**" + ctx.message.author.name + "**, you rolled a **" + str(random.randint(1,int(var[1]))) + "**!")
    elif len(var)>=2:
        if var[1].isdigit()==False:
            return await Autobot.say('**only positive integers may be used**')
        await Autobot.say("**" + ctx.message.author.name + "**, you rolled a **" + str(random.randint(1,int(var[1]))) + "**!")

@Autobot.command(pass_context=True , help= "google search")
async def google(ctx):
    print("?google command has been used" )
    await Autobot.say("https://www.google.com/search?q=" + ctx.message.content[8:].replace(" ", "+"))

@Autobot.command(pass_context=True , help = "makes a youtube search")
async def youtube(ctx):
    print("?youtube command has been used" )
    await Autobot.say("https://www.youtube.com/results?search_query=" + ctx.message.content[9:].replace(" ", "+"))

@Autobot.command(pass_context=True , help = "trump makes it illegal")
async def illegal(ctx):
    print("?illegal command has been used" )
    await Autobot.say("https://storage.googleapis.com/is-now-illegal.appspot.com/gifs/" + ctx.message.content[9:].upper().replace(" ", "+") + ".gif")

@Autobot.command(pass_context=True , help = "like another google search")
async def lmgtfy(ctx):
    print("?lmgtfy command has been used" )
    await Autobot.say("http://lmgtfy.com/?q=" + ctx.message.content[8:].replace(" ", "+"))

sloticons = [":pear:" , ":cherries:" , ":seven:" , ":apple:" , ":grapes:" , ":peach:" , ":tangerine:" , ":bell:" , ":cookie:" ,":pear:" , ":cherries:" , ":apple:" , ":grapes:" , ":peach:" , ":tangerine:" , ":cookie:" ,":pear:" , ":cherries:" , ":apple:" , ":grapes:" , ":peach:" , ":tangerine:" , ":bell:" , ":cookie:" ,] 



@Autobot.command(pass_context=True , help= "slot machine, still in the works")
async def slots(ctx):
    slotmachine = await Autobot.say(random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n" + "\n" + random.choice(sloticons) + "  |   " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n" + "\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons))
    await asyncio.sleep(0.5)
    await Autobot.edit_message(message=slotmachine, new_content = random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n" + "\n" + random.choice(sloticons) + "  |   " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n" + "\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons))
    await asyncio.sleep(0.2)  
    await Autobot.edit_message(message=slotmachine, new_content = random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n" + "\n" + random.choice(sloticons) + "  |   " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n" + "\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons))
    await asyncio.sleep(0.2)
    await Autobot.edit_message(message=slotmachine, new_content = random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n" + "\n" + random.choice(sloticons) + "  |   " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n" + "\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons))
    await asyncio.sleep(0.2)
    await Autobot.edit_message(message=slotmachine, new_content = random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n" + "\n" + random.choice(sloticons) + "  |   " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n" + "\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons))
    await asyncio.sleep(0.2)   
    await Autobot.edit_message(message=slotmachine, new_content = random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n" + "\n" + random.choice(sloticons) + "  |   " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n" + "\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons))

@Autobot.command(pass_context=True , help = 'slot command, in the works')
async def testslots(ctx):
    slotmachine2 = await Autobot.say( "\n**|   SLOT    MACHINE   |**"
"\n - - - - - - - - - - - - - - - -"
"\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + '\n'
"\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n"
"\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n   - - - - - **WIN** - - - - -")

    await Autobot.say(
    await asyncio.sleep(0.5) + await Autobot.edit_message(message=slotmachine2, new_content = "\n**|   SLOT    MACHINE   |**"
"\n - - - - - - - - - - - - - - - -"
"\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + '\n'
"\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n"
"\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n   - - - - - **WIN** - - - - -") + await asyncio.sleep(0.5) + await Autobot.edit_message(message=slotmachine2, new_content = "\n**|   SLOT    MACHINE   |**"
"\n - - - - - - - - - - - - - - - -"
"\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + '\n'
"\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n"
"\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n   - - - - - **WIN** - - - - -") + await asyncio.sleep(0.5) + await Autobot.edit_message(message=slotmachine2, new_content = "\n**|   SLOT    MACHINE   |**"
"\n - - - - - - - - - - - - - - - -"
"\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + '\n'
"\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n"
"\n" + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "  |  " + random.choice(sloticons) + "\n   - - - - - **WIN** - - - - -"))

@Autobot.command(pass_context=True , help= "deletes a large amount of messages")
async def purge(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).manage_messages == True:
        split = ctx.message.content.split(" ") 
        if len(split) == 1:
            await Autobot.say("**Must Provide a Number**")
        else:
            deletedmessage =  ctx.message.content.split(" ")[1]
            await Autobot.purge_from(ctx.message.channel , limit = int(deletedmessage),  check=None)

    else: Autobot.say("You don't have the **manage messages** permission!")

@Autobot.command(pass_context=True , help="kicks a certain user")
async def kick(ctx):
    print("?kick command was used by " + ctx.message.author.name)
    split = ctx.message.content.split(" ")
     
    if ctx.message.author.permissions_in(ctx.message.channel).kick_members == True:
        split = ctx.message.content.split(" ")
        if len(split) == 1:
            await Autobot.say("**Must Provide a User**")
        else:
            id = split[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
            member = ctx.message.server.get_member(id)
            if(member == None):
                return await Autobot.say("User not found!")
            try:
                await Autobot.kick(member)
                await Autobot.say("**Kicked** " + member.name)
            except:
                return await Autobot.say("**I don't have enough permissions**!!") 
    else:
        await Autobot.say("**You don't have enough permissions to kick someone!**")
@Autobot.command(pass_context=True, help= "bans a given user")
async def ban(ctx):
    print("?ban command was used by " + ctx.message.author.name + " to ban " + ctx.message.content.split(" ")[1])
    
    if ctx.message.author.permissions_in(ctx.message.channel).ban_members == True:
        split = ctx.message.content.split(" ") 
        if len(split) == 1:
            await Autobot.say("**Must Provide a User**")
        else:
            id = split[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
            member = ctx.message.server.get_member(id)
            if(member == None):
                return await Autobot.say("User not found!")
            try:
                await Autobot.ban(member , delete_message_days=1)
                await Autobot.say(member.name + " *Got the* **BAN HAMMER**")
            except:
                return await Autobot.say("*I don't have permissions!!*") 
    else:
        await Autobot.say("*You don't have enough permissions to ban someone!*")

@Autobot.command(pass_context = True , help = "my youtube playlist")
async def weebplaylist(ctx):
    print("?playlist command has been used by " + ctx.message.author.display_name + " in " + ctx.message.server.name)
    return await Autobot.say("http://www.youtube.com/playlist?list=PLEtcXcxy1h1zlhVhyVbtBN6lU6BnNH9tF")

@Autobot.command(pass_context = True , help = "my youtube playlist")
async def chillstep(ctx):
    print("?chillstep command has been used by " + ctx.message.author.display_name + " in " + ctx.message.server.name)
    return await Autobot.say("https://www.youtube.com/watch?v=qIN4jQ7TgmY&index=1&list=PLm7pUcK8LQsmU9vmMdkdY_tVVMUaumuMs&t=922s")





@Autobot.command(pass_context=True , help = "?nickname (name) changes your nickname")
async def nickname(ctx):
    await Autobot.change_nickname(ctx.message.author , ctx.message.content[10:])

@Autobot.command(pass_context=True , help = "?hehe (text) bot types the (text) and deletes your message")
async def hehe(ctx):
    await Autobot.say(ctx.message.content[6:])
    await Autobot.delete_message(ctx.message)

@Autobot.command(pass_context=True , help = "types lenny and deletes your message")
async def lenny(ctx):
    await Autobot.say("( ͡° ͜ʖ ͡°)")
    await Autobot.delete_message(ctx.message)

@Autobot.command(help = "slot machine, still in works")
async def qwerty():
    return await Autobot.say(
"\n**|   SLOT    MACHINE   |**"
"\n - - - - - - - - - - - - - - - -"
"\n   :banana:   |   :banana:   |   :banana:"
"\n"
"\n   :banana:   |   :banana:   |   :banana:"
"\n"
"\n   :banana:   |   :banana:   |   :banana:"
"\n   - - - - - **WIN** - - - - -")

@Autobot.command(help= "tell the bot to kys")
async def suicide():
    await Autobot.say("https://cdn.discordapp.com/attachments/258456438265872385/345755966475862046/unknown.png")

@Autobot.command(past_context=True , help= "creates a voice or text channel")
async def cchannel(ctx):
    await Autobot.create_channel(ctx.message.server, ctx.message.context.split(" ")[1], type=discord.ChannelType.voice)
    await Autobot.say("Created the **'" + ctx.message.content.split(" ")[1] + "'** Channel")

@Autobot.command(past_context=True , help= "creates a voice or text channel")
async def cchanneltest(ctx):
    await client.create_channel(ctx.message.server, 'Voice', type=discord.ChannelType.voice)

@Autobot.command()
async def pepe():
    await Autobot.say("```css"
    "\n__________████████_____██████"
"\n_________█░░░░░░░░██_██░░░░░░█"
"\n________█░░░░░░░░░░░█░░░░░░░░░█"
"\n_______█░░░░░░░███░░░█░░░░░░░░░█"
"\n_______█░░░░███░░░███░█░░░████░█"
"\n______█░░░██░░░░░░░░███░██░░░░██"
"\n_____█░░░░░░░░░░░░░░░░░█░░░░░░░░███"
"\n____█░░░░░░░░░░░░░██████░░░░░████░░█"
"\n____█░░░░░░░░░█████░░░████░░██░░██░░█"
"\n___██░░░░░░░███░░░░░░░░░░█░░░░░░░░███"
"\n__█░░░░░░░░░░░░░░█████████░░█████████"
"\n_█░░░░░░░░░░█████_████___████_█████___█"
"\n_█░░░░░░░░░░█______█_███__█_____███_█___█"
"\n█░░░░░░░░░░░░█___████_████____██_██████"
"\n░░░░░░░░░░░░░█████████░░░████████░░░█"
"\n░░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░░█"
"\n░░░░░░░░░░░░░░░░░░░░██░░░░█░░░░░░██"
"\n░░░░░░░░░░░░░░░░░░██░░░░░░░███████"
"\n░░░░░░░░░░░░░░░░██░░░░░░░░░░█░░░░░█"
"\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█"
"\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█"
"\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█"
"\n░░░░░░░░░░░█████████░░░░░░░░░░░░░░██"
"\n░░░░░░░░░░█▒▒▒▒▒▒▒▒███████████████▒▒█"
"\n░░░░░░░░░█▒▒███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█"
"\n░░░░░░░░░█▒▒▒▒▒▒▒▒▒█████████████████"
"\n░░░░░░░░░░████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█"
"\n░░░░░░░░░░░░░░░░░░██████████████████"
"\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█"
"\n██░░░░░░░░░░░░░░░░░░░░░░░░░░░██"
"\n▓██░░░░░░░░░░░░░░░░░░░░░░░░██"
"\n▓▓▓███░░░░░░░░░░░░░░░░░░░░█"
"\n▓▓▓▓▓▓███░░░░░░░░░░░░░░░██"
"\n▓▓▓▓▓▓▓▓▓███████████████▓▓█"
"\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██"
"\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"
"\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"
"\n"
"\nOoh oops! all these hot awesome maymays and you decided to look"
"\ninto these boring lines of codes? interesting indeed!"
"\nCan we argue that curiosity has deeper root in you than simply"
"\nseeking a few meaningless internet points?"
"\n```")

@Autobot.command(help= 'NO NORMIES')
async def normies():
    print("?normies command has been used" )
    return await Autobot.say("N    O     N    O    R    M    I    E    S"
    '\nO'
    '\n'
    '\nN'
    '\nO'
    '\nR'
    '\nM'
    '\nI'
    '\nE'
    '\nS')

@Autobot.command(pass_context= True , help = "gives you a role")
async def iam(ctx):
    print("The ?iam command has been used")
    role_name = ctx.message.content[5:].lower()
    for role in ctx.message.server.roles:
        if role.name.lower() == role_name:
            await Autobot.add_roles(ctx.message.author , role)
            await Autobot.send_message(ctx.message.channel , "added the **" + ctx.message.content[5:] + "** role!")

@Autobot.command(pass_context= True , help = "mutes a user")
async def mute(ctx):
    print("The ?mute command has been used to mute "  + ctx.message.content.split(" ")[1].nick)
    role_name = "muted"
    for role in ctx.message.server.roles:
        if role_name.lower() == "muted":
            
            id = ctx.message.content.split(" ")[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
            member = ctx.message.server.get_member(id)
            
            await Autobot.add_roles(member , role_name)

@Autobot.command(pass_context= True , help = "takes away a role")
async def imnot(ctx):
    print("The ?imnot command has been used")
    role_name = ctx.message.content[7:]
    for role in ctx.message.server.roles:
        if role.name.lower() == role_name:
            await Autobot.remove_roles(ctx.message.author , role)

@Autobot.command(pass_context= True , help = "creates a role")
async def makerole(ctx):
    print("The ?makerole command has been used by " + ctx.message.author.name)
    await Autobot.create_role(ctx.message.server , name = ctx.message.content[10:])

#@Autobot.command(pass_context= True , help = "takes away a role")
#async def editrole(ctx):
    #print("The ?editrole command has been used")
    #role_name = ctx.message.content[10:]
    #for role in ctx.message.server.roles:
        #if role.name.lower() == role_name:
            #await Autobot.edit_role(ctx.message.server , role, color = discord.Color(0x + ctx.message.content.split(" ")[2]) 
            # do this when i get the chance


gengar_pic  =  "https://imgur.com/asTuRbY"
snorlax_pic  =  "https://imgur.com/F341vzr"
dratini_pic =  "https://imgur.com/I4Qkj3O"
bulbasaur_pic=  "https://imgur.com/8nRzSR1"
pikachu_pic=  "https://imgur.com/tIwsMRC"
zubat_pic  = "https://imgur.com/YZ2xfgP"
vulpix_pic = "https://imgur.com/GkfA41i"
ekans_pic = "http://imgur.com/YPVk7D2"
magikarp_pic = "http://imgur.com/7OpnCJH"
gyarados_pic = "http://imgur.com/4ZROmsR"
eevee_pic = "http://imgur.com/WV1ACEL"
pidgey_pic = "http://imgur.com/HI1RtAe"
sphinx_pic = "http://imgur.com/yYmBOaX"
meowth_pic = "http://imgur.com/uFHjhDE"
squirtle_pic = "http://imgur.com/jyDtYFc"
lucario_pic = "http://imgur.com/bfNIKsY"
seadra_pic = "http://imgur.com/AC6ecQs"
dragonite_pic = "http://imgur.com/h26b4al"
jigglypuff_pic = "http://imgur.com/5QdEcLt"
dragonair_pic = "http://imgur.com/i2ndxiA"
sandslash_pic = "http://imgur.com/5tbDZPy"
ponyta_pic = "http://imgur.com/Y4iwPIb"
weedle_pic = "http://imgur.com/YT9XFhm"
hitmonchan_pic = "http://imgur.com/5tNKqAF"
hypno_pic = "http://imgur.com/8H5R1mS"
staryu_pic = "http://imgur.com/tD0QTu7"
abra_pic = "http://imgur.com/oJfjXp2"
rattata_pic = "http://imgur.com/8LPnm6H"
oddish_pic = "http://imgur.com/LXkMqzj"

pokemon ={oddish_pic:"oddish", rattata_pic:"rattata" , abra_pic:"abra",  staryu_pic: "staryu", 
hypno_pic: "hypno",  hitmonchan_pic: "hitmonchan", weedle_pic:"weedle" , ponyta_pic: "ponyta" , 
sandslash_pic: "sandslash" , dragonair_pic:"dragonair" , jigglypuff_pic: "jigglypuff" , 
dragonite_pic:"dragonite",  seadra_pic:"seadra" ,  lucario_pic:"lucario",  bulbasaur_pic:"bulbasaur",  
squirtle_pic:"squirtle", meowth_pic:"meowth", sphinx_pic: "shinx" , vulpix_pic:"vulpix" , 
dratini_pic:"dratini" , gengar_pic: "gengar", snorlax_pic: "snorlax",  pikachu_pic: "pikachu", 
ekans_pic: "ekans", magikarp_pic : "magikarp", gyarados_pic : "gyarados" , pidgey_pic: "pidgey" , 
eevee_pic: "eevee" ,  }

usaflag = "http://imgur.com/ru2CnAK"
australia = "http://imgur.com/3Qtdk0p"
argentina = "http://imgur.com/viFAVYq"
bolivia = "http://imgur.com/ZW8yRxw"
brazil = "http://imgur.com/yBlzXUd"
chile = "http://imgur.com/PH93aYD"
colombia = "http://imgur.com/RVqfPre"
costa_rica = "http://imgur.com/UQG7vWD"
china = "http://imgur.com/BfXS2Ph"
czech_republic = "http://imgur.com/UuCa7wy"
cuba_flag = "http://imgur.com/EWhXaxe"
dominican_republic = "http://imgur.com/L8n2LGp"
denmark = "http://imgur.com/oHc09Jz"
ecuador = "http://imgur.com/PFLbxoP"
egypt = "http://imgur.com/0vSuvNr"
ethiopia = "http://imgur.com/aaJelvU"
france = "http://imgur.com/RMy9eem"
finland = "http://imgur.com/GX8zaC7"
germany = "http://imgur.com/sYQokai"
greece = "http://imgur.com/DcNCRrh"
greenland = "http://imgur.com/K1meBYD"
hungary = "http://imgur.com/CkNKCMm"
iceland = "http://imgur.com/r7avvL9"
iraq = "http://imgur.com/g1vaZAJ"
italy = "http://imgur.com/gJnDS6d"
ireland = "http://imgur.com/IxlTsAr"
india = "http://imgur.com/Hmo822H"
israel = "http://imgur.com/yrV9iYd"
japan = "http://imgur.com/3aJT5Jk"
kekistan = "http://imgur.com/wQe1rJw"
mexico = "http://imgur.com/nqLpwUE"
nicaragua = "http://imgur.com/PW8lEdK"
peru = "http://imgur.com/GnxiPCz"
portugal = "http://imgur.com/RKau5PL"
swiss = "http://imgur.com/9e78AXk"
spain = "http://imgur.com/PwMEXvh"
sweden = "http://imgur.com/BDenB8s"
singapore = "http://imgur.com/kFNeGIX"
turkey = "http://imgur.com/mD9WPy0"
thailand = "http://imgur.com/iyn54lZ"
uk = "http://imgur.com/wrhMNAk"


worldflags = {usaflag: "usa;us;united states", australia: "australia" , argentina: "argentina" , bolivia: "bolivia" ,
 brazil: "brazil" , chile: "chile" , colombia : "colombia" , costa_rica: "costa rica" , china: "china" , 
 czech_republic: "czech republic" , cuba_flag: "cuba" , dominican_republic: "dominican republic" , denmark:
 "denmark" , ecuador: "ecuador" , egypt:"egypt" , ethiopia: "ethiopia" , france:"france" , finland: "finland",  germany:"germany" , greece:"greece" , greenland: "greenland" , hungary: "hungary" , iceland: "iceland" , 
  iraq : "iraq" , italy: "italy" , ireland: "ireland" , india: "india" , israel:"israel" , japan: "japan" , 
   kekistan:"kekistan" , mexico: "mexico" , nicaragua:"nicaragua" ,  peru:"peru" , portugal:"portugal" , 
   swiss:"switzerland" , spain:"spain" , sweden:"sweden" , singapore:"singapore" , turkey:"turkey" , 
   thailand:"thailand" , uk:"uk;britian"  }


deku = "http://imgur.com/jcgWTd2"
misuzu = "http://imgur.com/uwlpzRA"
esdeath = "http://imgur.com/HOpqOfv"
akame = "http://imgur.com/8jTulg4"
kanade = "http://imgur.com/J3Jz9vf"
yuri = "http://imgur.com/AztmRLD"
satoru = "http://imgur.com/gGf1I7I"
kayo = "http://imgur.com/iVGFUAT"
bakugou = "http://imgur.com/L6RKR0Z"
uraraka = "http://imgur.com/HSMwHsa"
tzuyu = "http://imgur.com/AiqHXzS"
nagisa = "http://imgur.com/7GaTboe"
tomoya = "http://imgur.com/XDa5m2G"
roka = "http://imgur.com/odqVAHG"
L = "http://imgur.com/7HSxHHW"
light = "http://imgur.com/PqM7sVQ"
lucy = "http://imgur.com/okFO8Yn"
sagiri = "http://imgur.com/Lk5EEN3"

animecharacter = {deku: "deku;midoriya" , misuzu:"misuzu" , esdeath:"esdeath" , akame:"akame" , kanade:"kanade" , yuri : "yuri" , satoru:"satoru" , kayo:"kayo" , bakugou:"bakugou" , uraraka:"uraraka" , tzuyu: "tzuyu;tzu;froppy" , nagisa:"nagisa" , tomoya:"tomoya;okazaki" , roka:"roka" , L: "L" , light:"light;yagami;yagami light;light yagami" , lucy:"lucy" , sagiri:"sagiri" , }




@Autobot.command(pass_context= True , help = "trivia, type ?trivia for trivia list")
async def trivia(ctx):
    if len(ctx.message.content.split(" ")) == 1:    return await Autobot.send_message(ctx.message.channel, "**Must include a trivia game! , type ?trivia (game)** \n \n List of Trivia Games:\n-**pokemon**\n-**flags** \n-**anime**")
    trivia1 = ctx.message.content.split(" ")[1].lower()
    if trivia1 == "pokemon":
        pokemon_trivia = await Autobot.say("You picked the **Pokemon** trivia game!")
        await asyncio.sleep(5)
        gamestart = await Autobot.say("Game Starting in **5**")
        await Autobot.edit_message(message= gamestart, new_content = "Game Starting in **4**")
        await asyncio.sleep(1)
        await Autobot.edit_message(message= gamestart, new_content = "Game Starting in **3**")
        await asyncio.sleep(1)
        await Autobot.edit_message(message= gamestart , new_content = "Game Starting in **2**")
        await asyncio.sleep(1)
        await Autobot.edit_message(message= gamestart, new_content = "Game Starting in **1**")
        await asyncio.sleep(1)

        repeat = []
        dict = {}
        while True:
            if len(repeat) == len(list(pokemon.keys())):
                await Autobot.send_message(ctx.message.channel, "ran out of questions, recycling old questions...")
                repeat.clear()
            num = random.randint(1, len(list(pokemon.keys())))
            
            while num in repeat:
                num = random.randint(1, len(list(pokemon.keys())))
            repeat.append(num)
            key = list(pokemon.keys())[num-1]
            await Autobot.send_message(ctx.message.channel, "What is this Pokemon? \n" + key)
            def check(msg):
                return msg.content.lower() == pokemon[key]
            waitmsg = await Autobot.wait_for_message(15, channel=ctx.message.channel, check=check)    
            if waitmsg == None:
                    await Autobot.send_message(ctx.message.channel, "No one guessed it right?! The answer was: " + pokemon[key])
            else:
                await Autobot.send_message(ctx.message.channel, waitmsg.author.name + " guessed it right! The answer was: " + pokemon[key])
                if dict.get(waitmsg.author.id) == None:
                    dict[waitmsg.author.id] = 1
                else:
                    dict[waitmsg.author.id] = dict[waitmsg.author.id] + 1
                    
                    if dict[waitmsg.author.id] == 10:
                        sorted_d = sorted(dict.items(), key=operator.itemgetter(1))
                        endscores = "```"

                        for key in sorted_d:
                            endscores = endscores + ctx.message.server.get_member(key[0]).name + " " + str(key[1]) + "\n"
                        return await Autobot.send_message(ctx.message.channel, endscores + "```") 


            await asyncio.sleep(5)
    trivia1 = ctx.message.content.split(" ")[1].lower()
    if trivia1 == "flags":
        pokemon_trivia = await Autobot.say("You picked the **World Flags** trivia game!")
        await asyncio.sleep(5)
        gamestart = await Autobot.say("Game Starting in **5**")
        await asyncio.sleep(1)
        await Autobot.edit_message(message= gamestart, new_content = "Game Starting in **4**")
        await asyncio.sleep(1)
        await Autobot.edit_message(message= gamestart, new_content = "Game Starting in **3**")
        await asyncio.sleep(1)
        await Autobot.edit_message(message= gamestart , new_content = "Game Starting in **2**")
        await asyncio.sleep(1)
        await Autobot.edit_message(message= gamestart, new_content = "Game Starting in **1**")
        await asyncio.sleep(1)

        repeat = []
        dict = {}
        while True:
            if len(repeat) == len(list(worldflags.keys())):
                await Autobot.send_message(ctx.message.channel, "ran out of questions, recycling old questions...")
                repeat.clear()
            num = random.randint(1, len(list(worldflags.keys())))
            
            while num in repeat:
                num = random.randint(1, len(list(worldflags.keys())))
            repeat.append(num)
            key = list(worldflags.keys())[num-1]
            await Autobot.send_message(ctx.message.channel, "What is this Flag? \n" + key)
            def check(msg):
                return msg.content.lower() in worldflags[key].split(";")
            
            waitmsg = await Autobot.wait_for_message(15, channel=ctx.message.channel, check=check)
            
            if waitmsg == None:
                await Autobot.send_message(ctx.message.channel, "No one guessed it right?! The answer was: " + worldflags[key].split(";")[0])
            
            else:
                await Autobot.send_message(ctx.message.channel, waitmsg.author.name + " guessed it right! The answer was: " + worldflags[key].split(";")[0])
                if dict.get(waitmsg.author.id) == None:
                    dict[waitmsg.author.id] = 1
                else:
                    dict[waitmsg.author.id] = dict[waitmsg.author.id] + 1
                    
                    if dict[waitmsg.author.id] == 10:
                        sorted_d = sorted(dict.items(), key=operator.itemgetter(1))
                        endscores = "```py"

                        for key in sorted_d:
                            endscores = endscores + ctx.message.server.get_member(key[0]).name + " " + str(key[1]) + "\n"
                        return await Autobot.send_message(ctx.message.channel, endscores + "```") 
            await asyncio.sleep(5)
    
    trivia1 = ctx.message.content.split(" ")[1].lower()
    if trivia1 == "anime":
        pokemon_trivia = await Autobot.say("You picked the **Anime Main Character** trivia game!")
        await asyncio.sleep(5)
        gamestart = await Autobot.say("Game Starting in **5**")
        await asyncio.sleep(1)
        await Autobot.edit_message(message= gamestart, new_content = "Game Starting in **4**")
        await asyncio.sleep(1)
        await Autobot.edit_message(message= gamestart, new_content = "Game Starting in **3**")
        await asyncio.sleep(1)
        await Autobot.edit_message(message= gamestart , new_content = "Game Starting in **2**")
        await asyncio.sleep(1)
        await Autobot.edit_message(message= gamestart, new_content = "Game Starting in **1**")
        await asyncio.sleep(1)

        repeat = []
        dict = {}
        while True:
            if len(repeat) == len(list(animecharacter.keys())):
                await Autobot.send_message(ctx.message.channel, "ran out of questions, recycling old questions...")
                repeat.clear()
            num = random.randint(1, len(list(animecharacter.keys())))
            
            while num in repeat:
                num = random.randint(1, len(list(animecharacter.keys())))
            repeat.append(num)
            key = list(animecharacter.keys())[num-1]
            await Autobot.send_message(ctx.message.channel,  "What is this characters name? \n" + key)
            def check(msg):
                return msg.content.lower() in animecharacter[key].split(";")
            waitmsg = await Autobot.wait_for_message(15, channel=ctx.message.channel, check=check)
            if waitmsg == None:
                await Autobot.send_message(ctx.message.channel, "No one guessed it right?! The answer was: " + animecharacter[key].split(";"))
            else:
                await Autobot.send_message(ctx.message.channel, waitmsg.author.name + " guessed it right! The answer was: " + animecharacter[key].split(";"))
                if dict.get(waitmsg.author.id) == None:
                    dict[waitmsg.author.id] = 1
                else:
                    dict[waitmsg.author.id] = dict[waitmsg.author.id] + 1
                    
                    if dict[waitmsg.author.id] == 10:
                        sorted_d = sorted(dict.items(), key=operator.itemgetter(1))
                        endscores = "```"

                        for key in sorted_d:
                            endscores = endscores + ctx.message.server.get_member(key[0]).name + " " + str(key[1]) + "\n"
                        return await Autobot.send_message(ctx.message.channel, endscores + "```") 
            await asyncio.sleep(5)



@Autobot.command(pass_context = True)
async def avatar(ctx):
    if len(ctx.message.content.split(" ")) == 1:
        em = discord.Embed(title="test", description=None, colour=0xDEADBF )
        set_image(ctx.message.author.avatar_url.replace("?size=1024" , ""))
        em.set_author(name="Autobot", icon_url=Autobot.user.default_avatar_url)
        await Autobot.send_message(ctx.message.channel, embed=em)
    else:
        id = ctx.message.content.split(" ")[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
        member = ctx.message.server.get_member(id)
        await Autobot.say(member.avatar_url.replace("?size=1024" , ""))

@Autobot.command(pass_context = True)
async def userinfo(ctx):
    print("?userinfo was used")
    if len(ctx.message.content.split(" ")) == 1:
        await Autobot.say(
        "```" + ctx.message.author.name + ", Your discriminator is " + ctx.message.author.discriminator + "```")
    else:
        id = ctx.message.content.split(" ")[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
        member = ctx.message.server.get_member(id)
        await Autobot.say("```The person's discrim is **" + member.discriminator + "**```")



@Autobot.command(pass_context= True)
async def taste(ctx):
    print("?taste command has been used")
    await Autobot.say(ctx.message.content[7:] + " has shit taste")

numbers = "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" ,  'J' , "Q" , "K" , "A"
suits = ":hearts:" , ":spades:", ":clubs:" , ":diamonds:"
statistics = {":hearts:": 0, ":clubs:": 0, ":spade:": 0, ":diamond:": 0}
#random.choice(numbers) + random.choice(suits)
@Autobot.command(pass_context = True)
async def poker(ctx):
    cards2 = []
    cards = []
    while len(cards) != 5:
        cards.append(random.choice(numbers) + random.choice(suits))
    await Autobot.say("  |  ".join(cards))
    for card in cards:
        for suit in statistics.keys():
            if card.find(suit) != -1:
                statistics[suit] += 1
    if statistics[":hearts:" , ":spades:", ":clubs:" , ":diamonds:"] > 4:
        return await Autobot.say('You Won!')
    else: return await Autobot.say('You Lost :(')

@Autobot.command(pass_context = True)
async def embed(ctx):
    em = discord.Embed(title="test", description='My Embed Content.', colour=0xDEADBF)
    em.set_author(name='Someone', icon_url=Autobot.user.default_avatar_url)
    await Autobot.send_message(ctx.message.channel, embed=em)

rps_stuff = "rock" , "paper" , "scissors"
ps = "paper" , "scissors"
rp = "rock" , "paper"
rs = "rock" , "scissors"

@Autobot.command(pass_context= True)
async def rps(ctx):
    if random.choice(rps_stuff) == "scissors" == ctx.message.content.split(" ")[1]:
        if random.choice(rp) == "paper":
            await Autobot.say("paper! You win!")
        else:
            await Autobot.say("Rock! You Lose!")
    else:
        if random.choice(rps_stuff) == "paper" == ctx.message.content.split(" ")[1]:
            await Autobot.say("paper")
        else: 
            if random.choice(rps_stuff) == "rock" == ctx.message.content.split(" ")[1]:
                await Autobot.say("rock")

@Autobot.command(pass_context=True)
async def summon(ctx):
    await Autobot.join_voice_channel(ctx.message.author.voice_channel)

@Autobot.command(pass_context=True)
async def play(ctx):
    voice = await Autobot.join_voice_channel(ctx.message.author.voice_channel)
    player = await voice.create_ytdl_player(ctx.message.content.split(" ")[1])
    player.start()
    await Autobot.say("playing **Shadilay!**")

@Autobot.command(pass_context = True , help = "creates an instant invite for the server")
async def serverinvite(ctx):
    serverinvite = await Autobot.create_invite(ctx.message.server , max_age = 86400 , max_uses = 1)
    await Autobot.send_typing(ctx.message.channel)
    await asyncio.sleep(5)
    await Autobot.say(serverinvite)

# ip is  174.138.43.238
Autobot.run(hehehe)
