import os
import time
import json
import discord
import random
import asyncio
import operator
from discord.ext import commands

startup_extensions = ["fun", "administration" , "information"]
Autobot =commands.Bot(command_prefix ="?" , pm_help=True,  description = "A bot made by Itz Splash"  )

@Autobot.event
async def on_ready():
    print("Autobot is Online!, running version " + discord.__version__ + " of Discord.py")
    await asyncio.sleep(10)
    await Autobot.change_presence(game=discord.Game(name="Type ?help", type=1))

@Autobot.command(pass_context=True , help= 'to test if the bot is online')
async def ping(ctx):
    return await Autobot.say("Autobots, __**Transform and Rollout!**__")





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



@Autobot.command(pass_context=True, help= 'rolls a dice')
async def rolldice(ctx):
    rand_roll = ["1" , '2' , '3' , '4' , '5' , '6']
    return await Autobot.say('**' + ctx.message.author.name + '**' + " , your roll is **" + random.choice(rand_roll) + '**' )

Rem_photos = ['http://i.imgur.com/bl9iQsu.jpg' , 'http://i.imgur.com/Nsc5SlA.jpg' , 'http://i.imgur.com/APSU7Bw.jpg' , 'http://i.imgur.com/7wK9PZh.jpg' , 'http://i.imgur.com/EnPQosj.png' , 'http://i.imgur.com/0gr4nkC.jpg' , 'http://i.imgur.com/COqbGN9.jpg' , 'http://i.imgur.com/ASP7BI1.jpg' , 'http://i.imgur.com/dXF1RRG.jpg' , 'http://i.imgur.com/4fOgBsr.jpg' , 'http://i.imgur.com/burcdcN.jpg' , 'http://i.imgur.com/TCCnd8b.jpg' , 'http://i.imgur.com/e6gHCPF.jpg' , 'http://i.imgur.com/bpzTsE2.jpg' , 'http://i.imgur.com/DQJPS8x.jpg' , 'http://i.imgur.com/f7w4RDE.jpg' , 'http://i.imgur.com/yGMqPom.png' , 'http://i.imgur.com/IIG4tpO.jpg' , 'http://i.imgur.com/JQ9U6ix.jpg' , 'http://i.imgur.com/xQU78GY.jpg' , 'http://i.imgur.com/jvmBTXB.jpg' , 'http://i.imgur.com/SUyaU9L.jpg' , 'http://i.imgur.com/gr695hc.jpg' , 'http://i.imgur.com/BVno6l6.png' , 'http://i.imgur.com/Ffn0dyK.jpg' , 'http://i.imgur.com/Gznz3n0.jpg' ,' http://i.imgur.com/WBawS2J.jpg', 'http://i.imgur.com/Mv7fcC9.jpg', 'http://i.imgur.com/kt9YnWG.jpg', 'http://i.imgur.com/iOzFqgh.jpg', 'http://i.imgur.com/hNnO8OX.jpg', 'http://i.imgur.com/YBygo97.jpg', 'http://i.imgur.com/9Iaakhw.jpg', 'http://i.imgur.com/QT1BC8W.jpg', 'http://i.imgur.com/1H7k5m8.jpg', 'http://i.imgur.com/639OCxG.jpg', 'http://i.imgur.com/lz2IXrg.jpg', 'http://i.imgur.com/ZQ6tVyv.png', 'http://i.imgur.com/WZjkDU8.jpg', 'http://i.imgur.com/4GIw1ne.jpg', 'http://i.imgur.com/IoeK3aM.jpg' , 'http://i.imgur.com/HDUeD1F.png', 'http://i.imgur.com/azszJ2B.png', ]

@Autobot.command(pass_context=True, help= 'shows a random pick of Rem from Re:zero')
async def rem():
    print("?rem command has been used" )
    return await Autobot.say(random.choice(Rem_photos))


@Autobot.command(pass_context=True , help= "google search")
async def google(ctx):
    print("?google command has been used" )
    await Autobot.say("https://www.google.com/search?q=" + ctx.message.content[8:].replace(" ", "+"))

@Autobot.command(pass_context=True , help = "makes a youtube search")
async def youtube(ctx):
    print("?youtube command has been used" )
    await Autobot.say("https://www.youtube.com/results?search_query=" + ctx.message.content[9:].replace(" ", "+"))



@Autobot.command(pass_context=True , help = "like another google search")
async def lmgtfy(ctx):
    print("?lmgtfy command has been used" )
    await Autobot.say("http://lmgtfy.com/?q=" + ctx.message.content[8:].replace(" ", "+"))

playlists = "weeb" , "chill"
def check(msg):
    return msg.content.lower() in playlists







numbers = "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" ,  'J' , "Q" , "K" , "A"
suits = ":hearts:" , ":spades:", ":clubs:" , ":diamonds:"
statistics = {":hearts:": 0, ":clubs:": 0, ":spade:": 0, ":diamond:": 0}
#random.choice(numbers) + random.choice(suits)
@Autobot.command(pass_context = True , hidden = True)
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

@Autobot.command(pass_context = True, hidden = True)
async def embed(ctx):
    em = discord.Embed(title="test", description='My Embed Content.', colour=0xDEADBF)
    em.set_author(name='Someone', icon_url=Autobot.user.default_avatar_url)
    await Autobot.send_message(ctx.message.channel, embed=em)

rps_stuff = "rock" , "paper" , "scissors"
ps = "paper" , "scissors"
rp = "rock" , "paper"
rs = "rock" , "scissors"

@Autobot.command(pass_context= True, hidden = True)
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

@Autobot.command(pass_context=True, hidden = True)
async def summon(ctx):
    await Autobot.join_voice_channel(ctx.message.author.voice_channel)

@Autobot.command(pass_context=True , hidden = True)
async def play(ctx):
    voice = await Autobot.join_voice_channel(ctx.message.author.voice_channel)
    player = await voice.create_ytdl_player(ctx.message.content.split(" ")[1])
    player.start()
    await Autobot.say("playing **Shadilay!**")





@Autobot.command(pass_context = True, hidden = True)
async def playshit(ctx):
    voice = await Autobot.join_voice_channel(ctx.message.author.voice_channel)
    player = voice.create_ffmpeg_player(random.choice(songsss))
    player.start()


@Autobot.command(hidden = True , pass_context=True)
async def react(ctx):
    asyncio.sleep(5)
    msg = await Autobot.send_message(ctx.message.channel, 'React with thumbs up or thumbs down.')
    await Autobot.add_reaction(msg , "👍")
    await Autobot.add_reaction(msg , '👎')
    res = await Autobot.wait_for_reaction(['👍', '👎'], message=msg , user = ctx.message.author)
    await Autobot.send_message(ctx.message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))

@Autobot.command(pass_context = True, hidden = True)
async def dmmeboi(ctx):
    await Autobot.send_message(ctx.message.author , "hey uwu" )


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


worldflags = {usaflag: "usa" , australia: "australia" , argentina: "argentina" , bolivia: "bolivia" ,
brazil: "brazil" , chile: "chile" , colombia : "colombia" , costa_rica: "costa rica" , china: "china" , 
czech_republic: "czech republic" , cuba_flag: "cuba" , dominican_republic: "dominican republic" , denmark:
"denmark" , ecuador: "ecuador" , egypt:"egypt" , ethiopia: "ethiopia" , france:"france" , finland: "finland",  germany:"germany" , greece:"greece" , greenland: "greenland" , hungary: "hungary" , iceland: "iceland" , 
iraq : "iraq" , italy: "italy" , ireland: "ireland" , india: "india" , israel:"israel" , japan: "japan" , 
kekistan:"kekistan" , mexico: "mexico" , nicaragua:"nicaragua" ,  peru:"peru" , portugal:"portugal" , 
swiss:"switzerland" , spain:"spain" , sweden:"sweden" , singapore:"singapore" , turkey:"turkey" , 
thailand:"thailand" , uk:"uk"  }
	   
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
    if len(ctx.message.content.split(" ")) == 1:    
        return await Autobot.send_message(ctx.message.channel, "**Must include a trivia game! , type ?trivia (game)** \n  List of Trivia Games:\n-**pokemon**\n-**flags**\n-**anime** ")
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
                return msg.content.lower() == worldflags[key]
            waitmsg = await Autobot.wait_for_message(15, channel=ctx.message.channel, check=check)
            if waitmsg == None:
                await Autobot.send_message(ctx.message.channel, "No one guessed it right?! The answer was: " + worldflags[key])
            else:
                await Autobot.send_message(ctx.message.channel, waitmsg.author.name + " guessed it right! The answer was: " + worldflags[key])
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
            if waitmsg is None:
                await Autobot.send_message(ctx.message.channel, "No one guessed it right?! The answer was: " + animecharacter[key])
            else:
                await Autobot.send_message(ctx.message.channel, waitmsg.author.name + " guessed it right! The answer was: " + waitmsg.content)
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
	


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            Autobot.load_extension(extension.lower())
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension.lower(), exc))



# ip is  sumtin
Autobot.run("token")
