############################################  C.T.P. - discord bot  ##########################################

import discord
from discord.ext import commands
import random
from random import randrange
import asyncio
import praw
import datetime

import pytz
import threading
from itertools import cycle

ctp = ["ctp-guide"]
uru_guide = ["uru-guide"]
memes_ctrl = ["memes"]
reddit = praw.Reddit(client_id='FNpct8XLVG2LTg',
                     client_secret='UeA14hUpw7LoKlkqFU2QDLoWu8M',
                     username='CrimsonDevil333',
                     password='shashikant@1',
                     user_agent='my user agent')
def read_token():
    with open("token.txt","r") as f:
        lines =f.readlines()
        return lines[0].strip()
token = read_token()
def read_prefex():
    with open("prefex.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()
prefex = read_prefex()
bot = commands.Bot(command_prefix=prefex , case_insensitive=True)
bot.remove_command("help")



@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(bot.guilds)+79} servers | .help'))
    


""" Discontinued! 
async def check_reset_time(ctx):
        await bot.wait_until_ready()
        daily_reset_time = "19:30:00"
        time = daily_reset_time.split(":")
        ist = pytz.timezone('Asia/Kolkata')
        aware1 = datetime.datetime(2020,4,1,int(time[0]),int(time[1]),int(time[2]),0,pytz.timezone('Asia/Kolkata'))
        tocompare1 = datetime.time(aware1.hour, aware1.minute, aware1.second)

        daily_reset_time = "19:30:01"
        time = daily_reset_time.split(":")
        aware2 = datetime.datetime(2020,4,1,int(time[0]),int(time[1]),int(time[2]),0,pytz.timezone('Asia/Kolkata'))
        tocompare2 = datetime.time(aware2.hour, aware2.minute, aware2.second)

        while not bot.is_closed():
            start = datetime.datetime.now(tz=ist)
            start = datetime.time(start.hour, start.minute,start.second)
            if start == tocompare1 or start == tocompare2:
                await ctx.send(f"{ctx.message.author.mention} only 1hr is left for daily reset in MFF ofcz.")
                break
            await ctx.send(".ctp")
            await asyncio.sleep(10)
            
@bot.command(name='remind')
async def remind(ctx,data = None):
    bot.loop.create_task(check_reset_time(ctx))
    await ctx.send(f"Remainder is activated on the request of {ctx.message.author}")

"""
"""    n = ""
    a = 1
    async for guild in bot.fetch_guilds(limit=35):
        n = n + str(a) + ". " + str(guild.name) + "\n"
        a=int(a)+1
    await ctx.send(n)
"""
@bot.command(pass_context=True, aliases=["rank","ranks"])
async def top(ctx):

    guilds = await bot.fetch_guilds(limit=150).flatten()
    
    clr=(0x00b3ff,0xff1f1f,0xff1ff8,0x141cff,0x14ffb1,0x67ff14,0xffe014,0xff1814)
    clrs=random.choice(clr)
    embed = discord.Embed(title="Server Ranking",
                          description=f'This ranking is based on no of times bot is used per day!\n\n1. {guilds[0]}\n2. {guilds[1]}\n3. {guilds[2]}\n.4 {guilds[3]}\n5. {guilds[4]}\n',
                          color=clrs)
    embed.set_thumbnail(
        url="https://i.ibb.co/4WHBRtm/pngfind-com-anime-png-598288.png"
    )
    embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

#Help command
@bot.command(pass_context=True, aliases=['h'])
async def Help(ctx):
    if str(ctx.channel) in ctp:
        clr=(0x00b3ff,0xff1f1f,0xff1ff8,0x141cff,0x14ffb1,0x67ff14,0xffe014,0xff1814)
        clrs=random.choice(clr)
        embed = discord.Embed(title="This is CTP guide bot",
                              description='The prefix for Bot is " . " ',
                              color=clrs)
        embed.set_thumbnail(
            url="https://pngimage.net/wp-content/uploads/2018/06/guide-png-4.png"
        )
        embed.add_field(name='C.T.P.', value="There are 12 different type of CTP's \nIf you want to know about any particular ctp just type its name using prefex",inline=False)
        embed.add_field(name="Names of CTP ",value="Judgement - '.j' , '.judgement'\nGreed - '.g' , '.greed'\nInsight - '.i' , '.insight'\nRage - '.rage' , '.r'\nEnergy - '.energy' , '.e'\nRegenration - '.regenration' , '.regen'\nAuthority - '.authority' , '.a'\n"
                                                   "Destruction - '.destruction' , '.d'\nRefinement - '.refinement' , '.ref'\nTranscendence - '.transcendence' , '.trans'\n"
                                                   "Patience - '.patience' , '.p'\nVeteran - '.veteran' , '.v'\nLocation of ctp - '.location' , '.l'", inline=False)
        embed.add_field(name='CTP Chest',value="You can try your luck by rolling one of those ctp chest keep in mind No ctp of veteren is there in it \nUse '.ctp'",inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()


        await ctx.send(embed=embed)
    elif str(ctx.channel) in uru_guide:
        await ctx.send(f"```Hello this is odin's blessing help book.....\nPefix = '{prefex}'\nodin - to open odin box\nuru/ob blessing_name - to know about particular blessing\n(example - to know about heal '.uru heal')\nname - to know names of odin blessings if you dont know```")


@bot.command(pass_context=True, aliases=['memes'])
async def meme(ctx):
    if str(ctx.channel) in memes_ctrl:
        memes_submissions = memes_submissions = reddit.subreddit('Memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title="Meme Smashhhh....",
                              description=f'Todays meme coming right up on request of \n{ctx.message.author}',
                              color=0x00FFDA) 
        embed.set_thumbnail(
            url="https://i.ibb.co/cX0qSkJ/http-pluspng-com-img-png-meme-png-lol-png-transparent-image-931.png"
        )
        embed.set_image(
            url=submission.url
        )
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

#
@bot.command(pass_context=True, aliases=['marvelmemes','mavelmeme','mar'])
async def marvel(ctx):
    if str(ctx.channel) in memes_ctrl:
        memes_submissions = memes_submissions = reddit.subreddit('marvelmemes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title="Marvel Meme Smashhhh....",
                              description=f'Todays marvel meme coming right up on request of \n{ctx.message.author}',
                              color=0x47FF00) 
        embed.set_thumbnail(
            url="https://i.ibb.co/zRJydjc/pngguru-com.png"
        )
        embed.set_image(
            url=submission.url
        )
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

@bot.command(pass_context=True, aliases=['animes'])
async def anime(ctx):
    if str(ctx.channel) in memes_ctrl:
        memes_submissions = memes_submissions = reddit.subreddit('Animemes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title="Kawaii Animes Memes",
                              description=f'Kawaii Memes coming right up on request of \n{ctx.message.author}',
                              color=0xF91CD4) 
        embed.set_thumbnail(
            url="https://i.ibb.co/SyqCmJd/pngguru-com-1.png"
        )
        embed.set_image(
            url=submission.url
        )
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
@bot.command(pass_context = True,aliases=["dank"])
async def dank_memes(ctx):
    if str(ctx.channel) in memes_ctrl:
        memes_submissions = memes_submissions = reddit.subreddit('dankmemes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title="Dank Memes",
                              description=f'Ya danker here is your dank meme .... \n',
                              color=0xF91CD4) 
        embed.set_thumbnail(
            url="https://i.ibb.co/rtGzWNN/Png-Item-29573.png"
        )
        embed.set_image(
            url=submission.url
        )
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

#ctp command
@bot.command(pass_context=True)
async def CTP(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="You opened ctp chest",
                              description='Congratulations you got....',
                              color=0x541212)
        img=("https://images-ext-2.discordapp.net/external/YfVV20vl6Mj_Q4XLOmJm1nCrAWF8eFoqj4leIsURCYE/https/i.imgur.com/etw0hUL.png","https://images-ext-1.discordapp.net/external/YklWbDTPoe6AeXiArE7a0p4Lh93r0Fy5f6ghRlSdyZA/https/i.imgur.com/eVtYF8p.png","https://images-ext-2.discordapp.net/external/_5DOwPLfHgA2DvDWveGwe7i8sUkmcvsIEyf4hBBNnjc/https/i.imgur.com/75XVqes.png","https://images-ext-1.discordapp.net/external/_68_kCWy02q6RnGwVsMfMegZP8Qag2egsjqbxf5sBH4/https/i.imgur.com/J7dVhbw.png","https://images-ext-1.discordapp.net/external/VAwn2iQV-Gf9jCB2CqCbDA5G50kvJ1UWjR0GJq0L17s/https/i.imgur.com/IBIsuaE.png","https://images-ext-2.discordapp.net/external/Kn9aMzYw6CqpNshTkL__QLX_fJAFS-42ufMM-y1gWgA/https/i.imgur.com/TRsLAIl.png","https://images-ext-2.discordapp.net/external/Qj2h-IAyrHx7fbFyeVM397nyyu-VlmVrhgs6TrmOj4g/https/i.imgur.com/7K0Xz07.png","https://images-ext-2.discordapp.net/external/l13EMZL0jlp4vqI-dIdK0PlDV1_Z7XFXXQEg_lLGuQg/https/i.imgur.com/jYiGknu.png","https://images-ext-2.discordapp.net/external/uIcnLNGQHL_PUM99p83tca-ijFLjBdk3X1pg_mlNx6M/https/i.imgur.com/ylLLge9.png","https://images-ext-1.discordapp.net/external/xFgl3XSvluPfW-DezQ4Lwx--Pu5FIEnoIw04Ew54DI8/https/i.imgur.com/T6ryvUs.png","https://images-ext-1.discordapp.net/external/C8-VixGH4g8lfBwq9KUvFeJki44o-F2-qgW8tVZbF2E/https/i.imgur.com/Wp5xlsy.png")
        
        imgs=random.choice(img)
        embed.set_image(
            url=imgs
        )
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)


#ctp of greed
@bot.command(pass_context=True, aliases=['g'])
async def Greed(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="CTP of Greed",
                              description="This is a good pve ctp. This ctp is good for characters like (thanos,jean..) as this ctp works good in both pvp and sometimes as well as pve content.",
                              color=0x55B80B)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/l13EMZL0jlp4vqI-dIdK0PlDV1_Z7XFXXQEg_lLGuQg/https/i.imgur.com/jYiGknu.png")
        embed.add_field(name="Location", value='Custom Gear Chest, Selector: CTP (Advanced/New)', inline = False)
        embed.add_field(name='Stats at Maximum Roll', value ='• Applies to: Self\nGuard Break Immunity \n• Ignore Dodge +45%\n• Applies to: Self % chance when attacking \nApplies to: Self \n10% recovery of Max HP.\n150% increase to damage against COMBAT, BLAST-type characters. (5 sec.)\n150% increase to damage against SPEED, UNIVERSAL-type characters. (5 sec.)\n(Activates Damage increase effect in turn.)\nCooldown Time 12 seconds', inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

@bot.command(pass_context=True, aliases=['j','judge','judgemen'])
async def Judgement(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="CTP of Judgement",
                              description="An extremely powerful CTP for Pve characters with all attack and chain hit for characters  whose damage is based on elemental attacks (i.e. cyclops,luna snow etc) Lacks the ignore boss defence like rage so might be bad for characters like namor for in abx/wbu boosts the damage for 5sec on any skill with element better than energy atk but not better than rage for elemental characters",
                              color=0x010846)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/uIcnLNGQHL_PUM99p83tca-ijFLjBdk3X1pg_mlNx6M/https/i.imgur.com/ylLLge9.png")
        embed.add_field(name="Location", value='Custom Gear Chest, Selector: CTP (Advanced/New)', inline = False)
        embed.add_field(name='Stats at Maximum Roll', value ='• Applies to: Self\n• All Attacks +32% \n• Chain Hit Damage Dealt +20%\n• Activation Rate: 10% chance when attacking\nApplies to: Enemies \nDecreases All Resistance by 30%. (5 sec.)\nApplies to: Self\nIncreased damage to all element damage by +200%. (5 sec.)\nCooldown Time 7 seconds', inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

@bot.command(pass_context=True, aliases=['i','in','sight'])
async def insight(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="CTP of Insight",
                              description="Could be useful in pve game modes where you can add damage by having this obelisk on a support character or even a character with a good leadership Against world boss or Shadowland,  ABX\nThere maybe some usefulness maybe in PVP as well Except the fact that it doesn't have itgb",
                              color=0x5D0B6D)
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/xFgl3XSvluPfW-DezQ4Lwx--Pu5FIEnoIw04Ew54DI8/https/i.imgur.com/T6ryvUs.png")
        embed.add_field(name="Location", value='Custom Gear Chest, Selector: CTP (Advanced/New)', inline = False)
        embed.add_field(name='Stats at Maximum Roll', value ='• Max HP +34%\n• All Defense +39%\n• Activation Rate: 10% chance when attacking\n• Applies to: All Allies \nIncreases damage dealt to SUPER HERO-type characters by 20%. (5 sec.)\nIncreases damage dealt to SUPER VILLAIN-type characters by 20%. (5 sec.)\n(The effect that applies to all team members cannot be applied in duplicate.)\nCooldown Time 7 seconds', inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

#ctp of energy
@bot.command(pass_context=True, aliases=['e'])
async def Energy(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="CTP of Energy",
                              description="Good for any kind of character especially those who can cancel their skill without make the animation stopped. The Ignore Dodge stat is very good to help character fight against bosses with high Dodge rate such as Frost Beast in ABX Speed Villain/Hero or Corvus Glaive WBU",
                              color=0xff0000)
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/C8-VixGH4g8lfBwq9KUvFeJki44o-F2-qgW8tVZbF2E/https/i.imgur.com/Wp5xlsy.png")
        embed.add_field(name="Location", value='Cinematic Battle Reward(Mythic Hela, Killmonger), Story Mission 13 - 8 First Clear Reward, Custom Gear Chest', inline = False)
        embed.add_field(name='Stats at Maximum Roll', value ='• Ignore Dodge + 45 % \n• Critical Damage ↑ +45 % \n• Activation Rate: 10 % chance when attacking \nApplies to: Self Increases Chain Hit damage by 30 % when attacking.(5 sec.) Increases damage by 200 % for 1 attack(s).(5 sec.) Cooldown Time 7 seconds', inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

#ctp of rage
@bot.command(pass_context=True, aliases=['r'])
async def Rage(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="CTP of Rage",
                              description="This CTP has special damage proc buff that allow your character to receive Increases"
                                           " Damage buff for any skill when proc is activated. Therefore this CTP will be very great "
                                           "for character who can deal decent damage from all of their skill. Obviously CTP of Rage is not "
                                           "suitable for character who focusing their damage to one skill only (i.e Sharon Rogers, Gambit)",
                              color=0xee00ff)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/Qj2h-IAyrHx7fbFyeVM397nyyu-VlmVrhgs6TrmOj4g/https/i.imgur.com/7K0Xz07.png")
        embed.add_field(name="Location", value='custom Gear Chest, Legendary battle - Thanos type 6', inline = False)
        embed.add_field(name="Stats at Maximum Roll", value ="• Critical Rate ↑ +32%\n• Dodge ↑ +32%\n• Activation Rate: 20% chance when dealing critical attack \nApplies to: Self Ignores Boss's Damage Decrease by 60% (5 sec.) Increases 0.9% damage per 1% of Dodge Rate and Critical Rate, regardless of Guaranteed Dodge Rate and Guaranteed Critical Rate (5 sec.) Cooldown Time 7 seconds'", inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

#ctp of regenration
@bot.command(pass_context=True, aliases=['reg', 'regen'])
async def Regenration(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="CTP of Regenration",
                              description="Made for PvP character due to its defensive stat. It is best to give this CTP to character "
                                           "who has healing ability either as passive or active skill.",
                              color=0x15a80b)
        embed.set_thumbnail(
            url="https://images-ext-2.discordapp.net/external/Kn9aMzYw6CqpNshTkL__QLX_fJAFS-42ufMM-y1gWgA/https/i.imgur.com/TRsLAIl.png")
        embed.add_field(name="Location", value='custom Gear Chest, Carol type 6', inline=False)
        embed.add_field(name="Stats at Maximum Roll",
                        value="• Max HP ↑ +34% \n• Guard Break Immunity, Increase HP Regen by 90% \n• Activation Rate: when HP is below 50% \nGenerates a Shield that is 35% of Max HP and ignores Cancel and Pierce effects (5 sec.) Recover 10% of Max HP Cooldown Time 10 seconds",
                        inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

#ctp of authority
@bot.command(pass_context=True, aliases=['a', 'auth'])
async def authority(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="CTP of Authority",
                              description="A defensive version of CTP of Destruction, but without buff to pierce through defensive skill. "
                                           "Which makes this CTP only works for character who already has an ability to pierce. The offensive stat"
                                           " given might help character with low damage to kill enemy faster.",
                              color=0xf9dd24)
        embed.set_thumbnail(
            url="https://images-ext-1.discordapp.net/external/VAwn2iQV-Gf9jCB2CqCbDA5G50kvJ1UWjR0GJq0L17s/https/i.imgur.com/IBIsuaE.png")
        embed.add_field(name="Location", value='custom Gear Chest', inline=False)
        embed.add_field(name="Stats at Maximum Roll",
                        value="• Applies to: Self Guard Break Immunity \n• Critical Damage ↑ +45% \n• Activation Rate: when HP is below 50%: \nApplies to: Self Accumulates 100% of True Damage regardless of Defense and Dodge stats. The total true damage accumulated cannot exceed 10% of HP. (7 sec.) Increases Attack by +5% for each 1% of damage taken. (7 sec.) Invincible (5 sec.) Cooldown Time 10 seconds",
                        inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

#ctp of destruction
@bot.command(pass_context=True, aliases=['des', 'd'])
async def destruction(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="CTP of Destruction",
                              description="A hybrid CTP, providing stat for both PvP and PvE mode. Extremely good for character with high "
                                           "survivability but lacking ability to pierce through defensive buff. The Increase Damage buff will "
                                           "help character to compete in PvE mode as well.",
                              color=0xe01aa1)
        embed.set_thumbnail(
            url="https://images-ext-1.discordapp.net/external/_68_kCWy02q6RnGwVsMfMegZP8Qag2egsjqbxf5sBH4/https/i.imgur.com/J7dVhbw.png")
        embed.add_field(name="Location", value='custom Gear Chest', inline=False)
        embed.add_field(name="Stats at Maximum Roll",
                        value="• Critical Damage ↑ +45% \n• Applies to: Self \nGuard Break Immunity \n• Activation Rate: 10% chance when attacking \nApplies to: Self 30% chance to penetrate with SUPER ARMOR, BARRIER, ALL DAMAGE IMMUNE, INVINCIBLE effect. (5 sec.) Increases damage by 200% for 1 attack(s). (5 sec.) Cooldown Time 7 seconds ",
                        inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)



#ctp of refinement
@bot.command(pass_context=True, aliases=['ref', 'refine'])
async def refinement(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="CTP of Refinement",
                              description="With the Max HP stat and Recovery ability provided, this CTP is good for character who has high defense against"
                                       " certain attack but lack of ability to heal. But due to the absence of Immunity to Guard Break, this CTP is not suitable for PvP metas",
                              color=0xb5215c)
        embed.set_thumbnail(
            url="https://images-ext-2.discordapp.net/external/_5DOwPLfHgA2DvDWveGwe7i8sUkmcvsIEyf4hBBNnjc/https/i.imgur.com/75XVqes.png")
        embed.add_field(name="Location", value='Cinematic Battle Reward (Mythic Hulk, Shuri), Custom Gear Chest', inline=False)
        embed.add_field(name="Stats at Maximum Roll",
                        value="• Max HP ↑ +34% \n• Recovery Rate ↑ +90% \n• Activation Rate: when HP is below 50% \nApplies to: Self\nGuard against 6 hits (6 sec.) 20% Recovery of MAX HP.Cooldown Time 15 seconds",
                        inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


#ctp of veteran
@bot.command(pass_context=True, aliases=['vet', 'v'])
async def veteran(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="CTP of Veteran",
                              description="Hard to find but domination of all. It make a character god tier",
                              color=0xe4b91b)
        embed.set_thumbnail(
            url="https://images-ext-1.discordapp.net/external/-iTWZP55z2MjhN9c0V83cwiD90QIsqNHzySDuX2IaYs/https/i.imgur.com/CcJgA5g.png")
        embed.add_field(name="Location", value="Collector's Vault Event", inline=False)
        embed.add_field(name="Stats at Maximum Roll",
                        value="• Guard Break Immunity, Ignore Dodge, Critical Damage Increase +32% \n• Increases All Attacks and Defense +28% \n• Activation Rate: 15% chance when attacking\nApplies to: Self\nIncreases Chain Hit Damage by 40% when attacking. (5 sec.)Creates a Shield that is 30% of Max HP and ignores Cancel and Pierce effects. (3 sec.)Increases damage by 150% for 1 attack(s). (5 sec.)Cooldown Time 7 seconds",
                        inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)



#ctp of transcendence
@bot.command(pass_context=True, aliases=['t', 'trans'])
async def transcendence(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="CTP of Transcendence",
                              description="With the All Attack stat provided, this CTP is good for character who uses summon/clone as main damage dealer."
                                       " But due to the absence of Immunity to Guard Break, this CTP is not suitable for PvP metas.",
                              color=0x1394f6)
        embed.set_thumbnail(
            url="https://images-ext-1.discordapp.net/external/YklWbDTPoe6AeXiArE7a0p4Lh93r0Fy5f6ghRlSdyZA/https/i.imgur.com/eVtYF8p.png")
        embed.add_field(name="Location", value="Hidden Route Reward", inline=False)
        embed.add_field(name="Stats at Maximum Roll",
                        value="• All Attack ↑ +40%\n• Ignore Dodge +45%\n• Activation Rate: when HP is below 50%\nApplies to: Self\nDecreases the effect of Reflect by 50% Reflects effect(s): PHYSICAL REFLECT, ENERGY REFLECT (5 sec.) Invincible (5 sec.) Cooldown Time 10 seconds",
                        inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


#ctp of Patience
@bot.command(pass_context=True, aliases=['p','pai'])
async def Patience(ctx):
    if str(ctx.channel) in ctp:
        embed = discord.Embed(title="CTP of Patience",
                              description="With the All Attack stat provided, this CTP is good for character who uses summon/clone as main damage dealer."
                                       " But due to the absence of Immunity to Guard Break, this CTP is not suitable for PvP metas.",
                              color=0x39f613)
        embed.set_thumbnail(
            url="https://images-ext-2.discordapp.net/external/YfVV20vl6Mj_Q4XLOmJm1nCrAWF8eFoqj4leIsURCYE/https/i.imgur.com/etw0hUL.png")
        embed.add_field(name="Location", value="Boost Point Stage 2 Reward", inline=False)
        embed.add_field(name="Stats at Maximum Roll",
                        value="• All Attack ↑ +40%\n• Dodge ↑ +40%\n• Activation Rate: when HP is below 50%\nApplies to: Self\nDecreases the effect of Reflect by 50% Reflects effect(s): PHYSICAL REFLECT, ENERGY REFLECT (5 sec.) Invincible (5 sec.) Cooldown Time 10 seconds",
                        inline=False)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


#ctp of location
@bot.command(pass_context=True, aliases=['l', 'loc'])
async def location(ctx):
    if str(ctx.channel) in ctp:
        file = discord.File("ctp.jpg", filename="ctp.jpg")
        await ctx.channel.send("You can find ctp's at......",file=file)


@bot.command(pass_context=True, aliases=['u', 'ob'])
async def uru(ctx, * , reason =None):
    if str(ctx.channel) in uru_guide:
        if reason == 'heal':
            embed = discord.Embed(title="Odin's Blessing: Heal",
                                description="• HP - 348/+464\n• HP - 348/+464",
                                color=0x091DD1)
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/Grh28vgW8w48zr2g3zNKPsKaL7hJ6yR4mXyzMAOs3q0/https/i.imgur.com/wSG299Z.png")
            await ctx.send(embed=embed)
        elif reason == 'amplify' or reason == 'amlify':
            embed = discord.Embed(title="Odin's Blessing: Amplify",
                                description="• Energy Attack - 99/+132\n• Critical Dammage - 222/+296",
                                color=0x091DD1)
            embed.set_thumbnail(
                url="https://images-ext-2.discordapp.net/external/SDk3NC4i6J_GyU-OFlereLo-CeuJFQ0bwkxmXfFCwwM/https/i.imgur.com/j9PlUnW.png")
            await ctx.send(embed=embed)
        elif reason == 'magik' or reason == 'magic':
            embed = discord.Embed(title="Odin's Blessing: Magic",
                                description="• Energy Attack - 99/+132\n• Energy Attack - 99/+132",
                                color=0x091DD1)
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/aHzsK--MNelFbpmuwoKk0LjrPtKxVisebiAS8YofAOM/https/i.imgur.com/Id0Obuy.png")
            await ctx.send(embed=embed)
        elif reason == 'resist' or reason == 'ressist':
            embed = discord.Embed(title="Odin's Blessing: Resist",
                                description="• Energy Attack - 99/+132\n• Ignore Defense - 222/+296",
                                color=0x091DD1)
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/Of3cTVPaMnOflf1BSQLNM4WXeM4FYYMTARdfK6KZCzU/https/i.imgur.com/iSeRqtY.png")
            await ctx.send(embed=embed)
        elif reason == 'balanse' or reason == 'balance':
            embed = discord.Embed(title="Odin's Blessing: Balance",
                                description="• Physical Attack - 99/+132\n• Energy Attack - 99/+132",
                                color=0x09A92D)
            embed.set_thumbnail(
                url="https://images-ext-2.discordapp.net/external/dMH754PlNksZjR8-mocx7CFUi29zUaKDn2yCOwK2tCg/https/i.imgur.com/ToBzt8L.png")
            await ctx.send(embed=embed)
        elif reason == 'focus' or reason == 'foc':
            embed = discord.Embed(title="Odin's Blessing: Focus",
                                description="• Energy Attack - 99/+132\n• Critical Rate - 222/+296",
                                color=0x09A92D)
            embed.set_thumbnail(
                url="https://images-ext-2.discordapp.net/external/n_2uoklwZ_ees5vwf4Nka5uitEwvwJulTNyoeEQoqwg/https/i.imgur.com/AnSkI2b.png")
            await ctx.send(embed=embed)
        elif reason == 'insight' or reason == 'sight':
            embed = discord.Embed(title="Odin's Blessing: Insight",
                                description="• Energy Attack - 99/+132\n• Skill Cooldown - 222/+296",
                                color=0x09A92D)
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/F9j6ogbv8BkGKNwdHIX0DhZBu_ROpwEsPdBIcXvGlZI/https/i.imgur.com/RdmjEHu.png")
            await ctx.send(embed=embed)
        elif reason == 'wil' or reason == 'wiil' or reason == 'will':
            embed = discord.Embed(title="Odin's Blessing: Will",
                                description="• Physical Attack - 99/+132\n• Skill Cooldown - 222/+296",
                                color=0x09A92D)
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/wxPm_FugxmQqHg5PgPQuovHIbPV07ej-6rqGYSHrMFI/https/i.imgur.com/AvfAndU.png")
            await ctx.send(embed=embed)


        elif reason == 'fortitude' or reason == 'fortude' or reason == 'forti':
            embed = discord.Embed(title="Odin's Blessing: Fortitude",
                                description="• Physical Attack - 99/+132\n• Ignore defense - 222/+296",
                                color=0xDB200C)
            embed.set_thumbnail(
                url="https://images-ext-2.discordapp.net/external/m1oY46EYDLzf5K5li-CPOETimO4EFO1w63CL9lTYncE/https/i.imgur.com/Ac55FKz.png")
            await ctx.send(embed=embed)
        elif reason == 'steel' or reason == 'steal' or reason == 'stel':
            embed = discord.Embed(title="Odin's Blessing: Steel",
                                description="• Physical Attack - 99/+132\n• Critical Damage - 222/+296",
                                color=0xDB200C)
            embed.set_thumbnail(
                url="https://images-ext-2.discordapp.net/external/oIB1oEBRNF7TBmztBfUmUg4anvwe-8mNUo5pVTbzh6M/https/i.imgur.com/guEBSUZ.png")
            await ctx.send(embed=embed)
        elif reason == 'strike' or reason == 'streke' or reason == 'str':
            embed = discord.Embed(title="Odin's Blessing: Strike",
                                description="• Physical Attack - 99/+132\n• Physical Attack - 99/+132",
                                color=0xDB200C)
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/DTk4v33eebxa_UvurZOVhiiOqN4opNNY0xrUM6rrroE/https/i.imgur.com/olMSmjU.png")
            await ctx.send(embed=embed)
        elif reason == 'toughness' or reason == 'tough' or reason == 'toughnes':
            embed = discord.Embed(title="Odin's Blessing: Toughness",
                                description="• Physical Attack - 99/+132\n• Critical Rate - 222/+296",
                                color=0xDB200C)
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/rftLnTiKRQaEv8n7EpjYRiUaaLazZTHYJo5YgQ4BFvI/https/i.imgur.com/BMX35oF.png")
            await ctx.send(embed=embed)
        elif reason == None:
            await ctx.send(f"{ctx.message.author.mention} please at least enter Odin's Blessing name you want to search.")
        else:
            await ctx.send("please use Correct Keywords")

@bot.command(pass_context=True,aliases=['names'])
async def name(ctx):
    if str(ctx.channel) in uru_guide:
        embed = discord.Embed(title="Following are the names of available Odin's Blessings",
                              description='• Amplify\n• Heal\n• Magic\n• Resist\n• Balance\n• focus\n• Insight\n• Will\n• Fortitude\n• Steel\n• Strike\n• Toughness',
                              color=0xFF00C5) 
   
        await ctx.send(embed=embed)


obls = ("https://images-ext-1.discordapp.net/external/rftLnTiKRQaEv8n7EpjYRiUaaLazZTHYJo5YgQ4BFvI/https/i.imgur.com/BMX35oF.png","https://images-ext-1.discordapp.net/external/DTk4v33eebxa_UvurZOVhiiOqN4opNNY0xrUM6rrroE/https/i.imgur.com/olMSmjU.png","https://images-ext-2.discordapp.net/external/oIB1oEBRNF7TBmztBfUmUg4anvwe-8mNUo5pVTbzh6M/https/i.imgur.com/guEBSUZ.png","https://images-ext-2.discordapp.net/external/m1oY46EYDLzf5K5li-CPOETimO4EFO1w63CL9lTYncE/https/i.imgur.com/Ac55FKz.png","https://images-ext-1.discordapp.net/external/wxPm_FugxmQqHg5PgPQuovHIbPV07ej-6rqGYSHrMFI/https/i.imgur.com/AvfAndU.png","https://images-ext-1.discordapp.net/external/F9j6ogbv8BkGKNwdHIX0DhZBu_ROpwEsPdBIcXvGlZI/https/i.imgur.com/RdmjEHu.png","https://images-ext-2.discordapp.net/external/n_2uoklwZ_ees5vwf4Nka5uitEwvwJulTNyoeEQoqwg/https/i.imgur.com/AnSkI2b.png","https://images-ext-2.discordapp.net/external/dMH754PlNksZjR8-mocx7CFUi29zUaKDn2yCOwK2tCg/https/i.imgur.com/ToBzt8L.png","https://images-ext-1.discordapp.net/external/Of3cTVPaMnOflf1BSQLNM4WXeM4FYYMTARdfK6KZCzU/https/i.imgur.com/iSeRqtY.png","https://images-ext-1.discordapp.net/external/aHzsK--MNelFbpmuwoKk0LjrPtKxVisebiAS8YofAOM/https/i.imgur.com/Id0Obuy.png","https://images-ext-2.discordapp.net/external/SDk3NC4i6J_GyU-OFlereLo-CeuJFQ0bwkxmXfFCwwM/https/i.imgur.com/j9PlUnW.png","https://images-ext-1.discordapp.net/external/Grh28vgW8w48zr2g3zNKPsKaL7hJ6yR4mXyzMAOs3q0/https/i.imgur.com/wSG299Z.png")
@bot.command(pass_context=True, aliases=['bless','blessing','blessings','odin'])
async def odinbless(ctx):
    if str(ctx.channel) in uru_guide:
        embed = discord.Embed(title="You opened a Odin's Blessing chest wow!",
                              description='Congratulations you got....',
                              color=0x00EAFF)        
        imgs=random.choice(obls)
      
        embed.set_image(
            url=imgs
        )
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

bot.run(token)
