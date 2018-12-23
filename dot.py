import discord
from discord.ext.commands import Bot
from discord.ext  import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio 
import platform
import colorsys
import requests
import random
import functools
import datetime
import json
import aiohttp
import os, re, smtplib
from urllib.request import urlopen, Request
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType

client = Bot(description="dot is gay", command_prefix=".", pm_help = True)
client.remove_command('help')

			 
def is_owner(ctx):
    return ctx.message.author.id == "417403958814965771"
 
                                                                                                     
@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Help — Everything is in here.')
      embed.add_field(name = 'Who i am?',value ='<:joy:525410119199227915> | am Dot, with Fun, Nsfw, Moderation Commands — ``Prefix - .``',inline = False)   
      embed.add_field(name = 'Invite Link',value ="[Here you are](https://discordapp.com/api/oauth2/authorize?client_id=523787927113826305&permissions=8&scope=bot)")      
      embed.add_field(name = '🇬 = General (Main Help) ',value ='Any Fun Commands are here.',inline = False)    
      embed.add_field(name =' 🇲 = Moderation (Mod Help)',value ='Any Moderation Commands are here.', inline = False)
      embed.add_field(name =' 🇳 = Not Safe to Work (NSFW Help)', value='Any NSFW commands are here.',inline = False)
      embed.add_field(name ='🎶 = Musics (Music Help)', value='Any Music Commands are here.', inline = False)
      dmmessage = await client.send_message(author,embed=embed)
      reaction1 = '🇬'  
      reaction2 = '🇲' 
      reaction4 = '🎶'
      reaction3 = '🇳'	
     	
      await client.add_reaction(dmmessage, reaction1)
      await client.add_reaction(dmmessage, reaction2)
      await client.add_reaction(dmmessage, reaction3)
      await client.add_reaction(dmmessage, reaction4)
      await client.say('<:a_:524648895796740126> | What are you waiting for, just look at DMs..')
	
   
@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '🇬':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = '.ping',value='Dot send fast internet')
        embed.add_field(name = '.meme',value ='Dot send any meme, on website Reddit.')			
        embed.add_field(name = '.avatar',value ='Use like — ``.avatar @user`` | Dot send someone users profile picture.')	
        embed.add_field(name ='.serverinfo', value ='Dot send server information.')	
        embed.add_field(name = '.love',value ='Use like — ``.love @user @user2`` | Dot send someone Couple!')
        embed.add_field(name = '.fortnite', value ='Use like — ``.fortnite (nickname)`` | Dot send information at Fortnite.')
        embed.add_field(name = '.penis', value ='Dot send penis of your size')	
        embed.add_field(name = '.woof',value ='Dot send any dog, on random.dog! :3')    
        embed.add_field(name = '.meow',value ='Dot send any cat, on random.cat! :3')				   
        embed.add_field(name = '.hug', value ='Dot send couple in hugs | ``.hug @user``')
        embed.add_field(name = '.kiss', value ='Dot send couple in kisses | ``.kiss @user``') 
        embed.add_field(name = '.howgay', value ='``(Not Completed)`` | Dot send how you gay on % :gay_pride_flag:')			      
        my_msg = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(my_msg)
		             
      if reaction.emoji == '🇲':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Mod Help - Help Commands')
        embed.add_field(name = '.ban',value ='``(Administrator Permissions Needed)`` | Just ban someone user like this ``.ban @user (reason)``',inline = False)
        embed.add_field(name = '.warn',value ='``(Manage Messages Permissions Needed)`` | Just warn someone user like this ``.warn @user (reason)``',inline = False)
        embed.add_field(name = '.mute',value='``(Administrator Permissions Needed)`` | Just Mute someone user like this ``.mute @user 10``',inline = False)
        embed.add_field(name = '.say',value ='``(Administrator Permissions Needed)`` | Just say in this command like this ``.say hello``',inline = False)
        embed.add_field(name = '.clear',value ='``(Manage Messages Permissions Needed)`` | Just clear your message like this ``.clear 10``.',inline = False)
        react_message = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(react_message)    																								

      if reaction.emoji == '🇳':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='NSFW Help - Help Commands')
        embed.add_field(name = '.ass',value ='Dot sends randomly photo of ass',inline = False)
        embed.add_field(name = '.pgif',value ='Dot sends randomly porngif.',inline = False)    
        embed.add_field(name = '.boobs',value ='Dot sends randomly boobs.',inline = False) 
        react_message = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(react_message)
				             
      if reaction.emoji == '🎶':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Dot - Music Commands')    
        embed.add_field(".play", "Usage: ``.play`` <song name> Description: Music.", inline = False)
        embed.add_field(".skip", "Usage: `.skip` Description: To skip music.", inline = False)
        embed.add_field(".stop", "Usage: `.stop` Description: To Bot disconnected.", inline = False)
        embed .add_field(".song", "Usage: `.song` Description: To Check The Current playing song.", inline = False)
        embed.add_field(".queue", "Usage: `.queue` Description: To Check The Queue List.", inline = False)
        embed.add_field(".volume", "Usage: `.volume` Description: To See Volume.", inline = False)
        embed.add_field(".volume [Wert]", "Usage: `.volume` Description: To Changes the volume level to the specified value.", inline = False)			
        embed.add_field(".pause", "Usage: `.pause` Description: To pause The Current Playing Song.", inline = False)
        embed.add_field(".resume", "Usage: `.resume` Description: To Resume The Paused Song.", inline = False)
        embed.add_field(".mutemusic","Usage: `.mutemusic` Description: To mute Bot.", inline = False)
        embed.add_field(".unmutemusic", "Usage: `.unmutemusic` Description: To unmute Bot.", inline = False)
        react_message = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(react_message)    																								
		
@client.command(pass_context = True)
@commands.check(is_owner)
async def off():
    await client.close()
    
    	
@client.command()
async def ass():
		embed = embed = discord.Embed(title = "🚓 | FBI OPEN UP!", color = 0x7B68EE) 
		embed.set_image(url = random.choice(["https://nekobot.xyz/ass/h48sq9jdtzmax6kercvf.jpg","https://nekobot.xyz/ass/1ydlm9n0bzt7uopfxrig.jpg","https://nekobot.xyz/ass/s58k3y6tp0av2f4mu9d1.jpg","https://nekobot.xyz/ass/b3lzd7vungxsyjm42fk8.jpg","https://nekobot.xyz/ass/vjg0atkh1f5bdwxz6une.jpg","https://nekobot.xyz/ass/ewiq0g85dulbn9p2ycz1.jpg","https://nekobot.xyz/ass/hotnxaz9051gqrl7bdue.png","https://nekobot.xyz/ass/kr408gmj2t31hvq9xz5a.jpg","https://nekobot.xyz/ass/n9olr58ftbip7asjweyg.png","https://nekobot.xyz/ass/nr0ov1eqfgi62l5kucay.jpg","https://nekobot.xyz/ass/ndkjq52bsa4xmc3t9i0z.jpg"]))
		await client.say(embed=embed)	
			
@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name='.help | with '+str(len(set(client.get_all_members())))+' users', url="https://twitch.tv/myname", type=1))				
								                                         
		
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    await client.send_message(userName, "You have been warned for: **{}**".format(message))
    await client.say("**:white_check_mark: | {} has been warned!** ".format(userName,message))
    pass		
			
@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = []
         number = int(number)
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await client.delete_messages(mgs)          
        await client.say(+str(number)+  '| Messages deleted! cože')
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.say(':x: | Clear Failed.')
        return         
   
    await client.delete_messages(mgs)      

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def say(ctx, *args):
    argstr = " ".join(args)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    text = argstr
    color = discord.Color((r << 16) + (g << 8) + b)
    await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
    await client.delete_message(ctx.message) 

@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):

    if user.server_permissions.ban_members:
        await client.say('**:negative_squared_cross_mark: | User has been not banned!**')
        return

    try:
        await client.ban(user)
        await client.say('**:white_check_mark: | ' +user.name+ ' **has been banned! **')

    except discord.Forbidden:

        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('ban failed.')
        return

                           
@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
        embed.set_image(url = ctx.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_image(url = user.avatar_url)
        await client.say(embed=embed)                                                                                                                                                                                  	                    						
	
	
@client.command(pass_context=True)
async def meow(ctx):
    """Grabs a random cat picture"""
    for i in range(0,5):
        # site is buggy and sometimes gives bad images
        # just loop until we get a good one
        try:
            r = requests.get("https://aws.random.cat/meow")
            r = str(r.content)
            r = r.replace("b'","")
            r = r.replace("'","")
            r = r.replace("\\","")
            url = json.loads(r)["file"]
            await client.say(url)
            break
        except:
            pass	
	
	
@client.command(pass_context=True)
async def woof(ctx):
    """Because dogs are cute too"""
    r = requests.get("https://random.dog/woof")
    r = str(r.content)
    r = r.replace("b'","")
    r = r.replace("'","")
    await client.say("https://random.dog/" + r)
	
	
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def emojiids(ctx):
  for emoji in ctx.message.author.server.emojis:
    print(f"<:{emoji.name}:{emoji.id}>")
    print(" ")    	
				                 
@client.command(pass_context = True)
async def meme(ctx):
    colour = '0x' + '008000'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            embed = discord.Embed(title='Redditovski, Anal—ysis', description='', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)
		
@client.command()
async def boobs():
	embed = embed = discord.Embed(title = "Boobs is perfect", color=0x7B68EE)
	embed.set_image(url = random.choice(["https://i.imgur.com/xs51PQn.jpg","https://i.redd.it/4s4dg79yiwm11.jpg","https://i.redd.it/io24ypewg6201.jpg"]))

@client.command(pass_context=True)
async def love(ctx, user: discord.Member = None, *, user2: discord.Member = None):
    shipuser1 = user.name
    shipuser2 = user2.name
    useravatar1 = user.avatar_url
    useravatar2s = user2.avatar_url
    self_length = len(user.name)
    first_length = round(self_length / 2)
    first_half = user.name[0:first_length]
    usr_length = len(user2.name)
    second_length = round(usr_length / 2)
    second_half = user2.name[second_length:]
    finalName = first_half + second_half
    score = random.randint(0, 100)
    filled_progbar = round(score / 100 * 10)
    counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)
    url = f"https://nekobot.xyz/api/imagegen?type=ship&user1={useravatar1}&user2={useravatar2s}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f"{shipuser1} ❤ {shipuser2} love eath other", description=f"Love\n`{counter_}` Score:**{score}% **\nLove Name:**{finalName}**", color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            await client.say(embed=embed)


@client.command(pass_context=True)
async def howgay(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    howgay = [":gay_pride_flag: | You are 1% gay",":gay_pride_flag:  | You are 2% gay",":gay_pride_flag:  |  You are 100% gay",":gay_pride_flag: | You are 90% gay",":gay_pride_flag: | You are 50% gay",":gay_pride_flag: | You are 69% gay"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name=f"ur mom gay", value=random.choice(howgay))
    await client.say(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def mute(ctx, member: discord.Member=None, mutetime=None):
    if member is None:
        await client.say('Please specify member i.e. Mention a member to mute. Example-``mv!mute @user <time in minutes>``')
        return
    if mutetime is None:
        await client.say('Please specify time i.e. Mention a member to mute with time. Example-``mv!mute @user <time in minutes>``')
        return
    if member.server_permissions.kick_members:
        await client.say('**You cannot mute admin/moderator!**')
        return
    if ctx.message.author.bot:
      return
    else:
      mutetime =int(mutetime)
      mutetime = mutetime * 60
      output = mutetime/60
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.add_roles(member, role)
      await client.say("Muted **{}**".format(member.name))
      await client.send_message(member, "You are muted by {0} for {1} Minutes".format(ctx.message.author, output))
      for channel in member.server.channels:
        if channel.name == 'updates':
            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}** for {2} minutes!".format(member, ctx.message.author, output), color=0x37F60A)
            await client.send_message(channel, embed=embed)
            await asyncio.sleep(mutetime)
            await client.remove_roles(member, role)
            await client.say("Unmuted **{}**".format(member.name))
            embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted!".format(member, ctx.message.author), color=0xFD1600)
            await client.send_message(channel, embed=embed)

@client.command(pass_context=True)
async def ping(ctx):
    username = ctx.message.author.display_name
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    embed=discord.Embed(title="Pong at {username}".format(username=username), description='It took {}ms.'.format(round((t2-t1)*1000)), color=0xDA70D6)
    await client.say(embed=embed) 		                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 		                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    randomurl = ["https://media3.giphy.com/media/G3va31oEEnIkM/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media1.tenor.com/images/e4fcb11bc3f6585ecc70276cc325aa1c/tenor.gif?itemid=7386341", "http://25.media.tumblr.com/6a0377e5cab1c8695f8f115b756187a8/tumblr_msbc5kC6uD1s9g6xgo1_500.gif"]
    if user.id == ctx.message.author.id:
        await client.say("Goodluck kissing yourself {}".format(ctx.message.author.mention))
    else:
        embed = discord.Embed(title=f"{user.name} You just got a kiss from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)					
	

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'vítejte':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'Zdravím tě {member.name} v {member.server.name}!', description='Nezapomeň si prečíst <#524665183667224596> a <#524939736431853578>!', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='Děkujeme za připojení, na tento server!', value='Doufáme, že budes aktivní na tomto serveru!', inline=True)
            embed.set_image(url = member.avatar_url)
            embed.add_field(name='Připojovací Pozice', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Čas připojení', value=member.joined_at)
            await client.send_message(channel, embed=embed)     
            role = discord.utils.get(member.server.roles, name='∟ Návštěvník')
            await client.add_roles(member, role)             
                     
@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == 'vítejte':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} odešel z {member.server.name}', description='Doufáme, že se ti tu libílo!', color = discord.Color((r << 16) + (g << 8) + b))        
            embed.add_field(name='Vaše připojovací pozice byla', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await client.send_message(channel, embed=embed)				

@client.command()
async def pgif():
		embed = embed = discord.Embed(title = "Porngif is art. '", color = 0x7B68EE)
		embed.set_image(url = random.choice(["https://nekobot.xyz/pgif/v6ztr7l8a2ndqmgxkh19.gif","https://nekobot.xyz/pgif/lfkcadesnvjy9gzhi5tp.gif", "https://nekobot.xyz/pgif/2w04ul98vdxyt6airjc7.gif", "https://nekobot.xyz/pgif/od8gyclnzxt5kqebrs9u.gif","https://nekobot.xyz/pgif/atxb96wkeu4q3gzpnfm5.gif","https://nekobot.xyz/pgif/hjstg1lkodai75rpf8c4.gif", "https://nekobot.xyz/pgif/e8ib5h0uvwzljsd6na9k.gif","https://nekobot.xyz/pgif/mx5ako23d9ge4vpqzunf.gif"]))
		await client.say(embed=embed)                                         	
																				
@client.command(pass_context=True)     
async def serverinfo(ctx):
    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)
    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))
    roles = ', '.join(roles);
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    online = len([m.status for m in server.members if m.status == discord.Status.online or m.status == discord.Status.idle])
    embed = discord.Embed(name="{} Server information".format(server.name), color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url = server.icon_url)
    embed.add_field(name="• Server Info", value=server.name, inline=True)
    embed.add_field(name="• Owner", value=server.owner.mention)
    embed.add_field(name="• Server ID", value=server.id, inline=True)
    embed.add_field(name="• Roles", value=len(server.roles), inline=True)
    embed.add_field(name="• Members", value=len(server.members), inline=True)
    embed.add_field(name="• Online", value=f"**{online}/{len(server.members)}**")
    embed.add_field(name="• Created at", value=server.created_at.strftime("%d %b %Y %H:%M"))
    embed.add_field(name="• Emojis", value=f"{len(server.emojis)}/100")
    embed.add_field(name="• Server Region", value=str(server.region).title())
    embed.add_field(name="• Total Channels", value=len(server.channels))
    embed.add_field(name="• AFK Channel", value=str(server.afk_channel))
    embed.add_field(name="• AFK Timeout", value=server.afk_timeout)
    embed.add_field(name="• Verification Level", value=server.verification_level)
    embed.add_field(name="• Roles {}".format(role_length), value = roles)
    await client.send_message(ctx.message.channel, embed=embed)		

	
@client.command(pass_context=True)
async def hug(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if user.id == ctx.message.author.id:
        await client.say("{} Wanted to hug himself/herself , good luck on that you will look like an idiot trying to do it".format(user.mention))
    else:
        randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)		
        
@client.command(description="Fetches a player's Fortnite stats.")
async def fortnite(nickname):
    url = "https://api.fortnitetracker.com/v1/profile/pc/"+ nickname
    key = {'TRN-Api-Key' : 'de6135b6-43cb-40af-9985-872ae3cd6464'}
    response = requests.get(url, headers=key)
    #jsonData = json.loads(response.text)

    #platform = response.json()['platformNameLong']
    userName = response.json()['epicUserHandle']
    top5s = response.json()['lifeTimeStats'][0]['value']
    top3s = response.json()['lifeTimeStats'][1]['value']
    top10s = response.json()['lifeTimeStats'][3]['value']
    numMatches = response.json()['lifeTimeStats'][7]['value']
    wins = response.json()['lifeTimeStats'][8]['value']
    winPct = response.json()['lifeTimeStats'][9]['value']
    kills = response.json()['lifeTimeStats'][10]['value']
    kd = response.json()['lifeTimeStats'][11]['value']

    await client.say(userName+"'s stats: " + "\n"
                     + "Number of matches: " + str(numMatches) + "\n"
                     + "Top 10s: " + str(top10s) + "\n"
                     + "Top 5s: " + str(top5s)  + "\n"
                     + "Top 3s: " + str(top3s) + "\n"
                     + "Wins: " + str(wins) + "\n"
                     + "Win percentage: " + str(winPct) + "\n"
                     + "Kills: " + str(kills) + "\n"
                     + "K/D: " + str(kd) + "\n")        

@client.command(pass_context=True)
async def penis(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    penis = ["8=D"," 8==D","8===D","8=============D","8=======D","8===============D"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name=f"penis machine fam", value=random.choice(penis))
    await client.say(embed=embed)
                            
client.run(os.getenv('Token'))
		                                                                                                
