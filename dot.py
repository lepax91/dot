import discord
from discord.ext.commands import Bot
from discord.ext  import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio 
import platform
import colorsys
import requests
import sys
import random
import functools
import praw
import datetime
import json
import traceback 
import aiohttp
import os, re, smtplib
from urllib.request import urlopen, Request
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType



start_time = datetime.datetime.utcnow()

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""
    prefixes = ['.','dot ']   
    return commands.when_mentioned_or(*prefixes)(bot, message)
HOST = '' 
PORT = os.environ["PORT"] 
TOKEN = os.environ["TOKEN"]

try:
    s.bind((HOST,PORT))
except Exception as e:
    print(e)
client = discord.Client()
client = commands.Bot(command_prefix=get_prefix)
client.remove_command('help')
#()  []  {} `
init_extensions = ['cogs.error_handler','cogs.wiki','cogs.fun','cogs.images']

if __name__ == '__main__':
    for extension in init_extensions:
        try:
            client.load_extension(extension)
            print(f'Nacteno {extension}')
        except Exception as e:
            print(f'Nepodarilo se nacist {extension}.', file=sys.stderr)
            traceback.print_exc()
		
def is_owner(ctx):
    return ctx.message.author.id == "417403958814965771"

@client.command(pass_context=True, no_pm=True)
async def info(ctx):	    
    em = discord.Embed(color=discord.Color.purple())
    em.title = 'Informations of Dot'
    em.add_field(name="Servers", value=len(client.servers))
    em.add_field(name="<:3619_discord_online:538667013803999232> Online Users", value=str(len({m.id for m in client.get_all_members() if m.status is not discord.Status.offline})))
    em.add_field(name='Channels', value=f"{sum(1 for g in client.servers for _ in g.channels)}")
    em.add_field(name="Library", value=f"discord.py")
    em.add_field(name="Development of Dot", value=f"<@417403958814965771>")
    em.add_field(name="Help with Support Server!", value=f"<@273813194861051907> (Channels, Roles)")
    em.add_field(name="Invite dot to next server!", value=f"[Here](https://discordapp.com/oauth2/authorize?client_id={client.user.id}&scope=bot&permissions=268905542)")
    em.add_field(name="Do not forget to vote for Dot!", value=f"[Here](https://divinediscordbots.com/bots/523787927113826305)",inline=False)
    em.add_field(name="If you have problems with Dot", value=f"[Join Here!](https://discord.gg/XQW9uf2)")
    em.set_footer(text="Dot | Pre-Alpha 1.2")
    await client.say(embed=em)
				
@client.command(pass_context=True, no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def urban(ctx, *, msg:str=None):
    await client.send_typing(ctx.message.channel)
    if msg is None:
        await client.say('Use it like: ``.urban <string>``')
        return
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
        response = requests.get(api, params=[("term", word)]).json()
        if len(response["list"]) == 0:
            return await client.say("Could not find that word!")
        embed = discord.Embed(title = "🔍 Search Word", description = word, color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = "Top definition:", value = response['list'][0]['definition'])
        embed.add_field(name = "Examples:", value = response['list'][0]["example"])    
        await client.say(embed=embed)
			
		
@client.event
async def on_ready():
    print("The bot is ready!")
    print("Connected on " + str(len(client.servers)) + " servers:") 
    await client.change_presence(game=discord.Game(name='.help || '+str(len(set(client.get_all_members())))+' users || '+str(len(client.servers))+' servers', type=3))
							
@client.command(pass_context=True,no_pm=True)
async def quit(ctx):
    if str(ctx.message.author) != "lepax_#1234":
        await client.say("Hey! You can't do that!'")
        return
    else:
        await client.say("See you later bye!")
        await client.logout()

@client.command()
async def play():
	print('hm?')
	
@client.command()
async def stop():
	print('hm?!')	
		
@client.command(pass_context = True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def coinflip(ctx):
    choices = ['https://upload.wikimedia.org/wikipedia/commons/4/44/2014_ATB_Quarter_Obv.png', 'http://fracademic.com/pictures/frwiki/50/2005_Half_Dollar_Rev_Unc_P.png']
    color = discord.Color(value=0x00ff00)
    embed = discord.Embed(color=color, title='Flipped a coin!')
    embed.set_image(url=random.choice(choices))
    await client.say(embed=embed)


@client.command(pass_context=True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@commands.has_permissions(ban_members=True)     
async def unban(ctx, identification:str):
    user = await client.get_user_info(identification)
    await client.unban(ctx.message.server, user)
    try:
        await client.say(f'**:white_check_mark: | {user} has been unbanned!**')
        for channel in ctx.message.server.channels:
          if channel.name == 'log':
              embed=discord.Embed(title="User unbanned!", description="**{0}** unbanned by **{1}**!".format(user, ctx.message.author), color=0x38761D)
              await client.send_message(channel, embed=embed)
    except:
        await client.say(f':x: | Unable to unban *{user}*')
        pass
  
@client.command(pass_context = True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    await client.send_message(userName, "You have been warned for: **{}**".format(message))
    await client.say("**:white_check_mark: | {} has been warned!** ".format(userName,message))
    pass		
			

		
@client.command(pass_context = True,no_pm=True)
async def cosplay(ctx):
    colour = '0x' + 'ff96a9'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/Cosporn/random") as r:
            data = await r.json()
            embed = discord.Embed(title='', description='', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)	
	
	
	
	
@client.command(pass_context=True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def say(ctx, *args):
    argstr = " ".join(args)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    text = argstr
    color = discord.Color((r << 16) + (g << 8) + b)
    await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
    await client.delete_message(ctx.message) 

@client.command(pass_context=True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
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
        pass


	
	
@client.command(pass_context=True, no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def avatar(ctx, member: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title='', description='', color=discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url="{}".format(member.avatar_url))
    await client.say(embed=embed)     
	
	
@client.command(pass_context = True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def meme(ctx):
    colour = '0x' + '008000'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/dankmemes/random") as r:
            data = await r.json()
            embed = discord.Embed(title='', description='', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)	      		
	
@client.command(pass_context=True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def uptime(ctx: commands.Context):
    now = datetime.datetime.utcnow() # Timestamp of when uptime function is run ji
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await client.say("{} has been up for {}".format(client.user.name, uptime_stamp))

			
@client.command(pass_context = True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def kick(ctx, userName: discord.User):
    await client.kick(userName)	
		
@client.command(pass_context = True,no_pm=True)
async def emojiids(ctx):
  for emoji in ctx.message.author.server.emojis:
    print(f"<:{emoji.name}:{emoji.id}>")
    print(" ")    					                 
						
@client.command(pass_context=True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
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


@client.command(pass_context=True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def howgay(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    howgay = [":gay_pride_flag: | You are 1% gay",":gay_pride_flag:  | You are 2% gay",":gay_pride_flag:  |  You are 100% gay",":gay_pride_flag: | You are 90% gay",":gay_pride_flag: | You are 50% gay",":gay_pride_flag: | You are 69% gay"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name=f"ur mom gay", value=random.choice(howgay))
    await client.say(embed=embed)

@client.command(pass_context = True,no_pm=True)
async def butt(ctx):
    colour = '0x' + '00fffa'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/ass/random") as r:
            data = await r.json()
            embed = discord.Embed(title='', description='', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])         
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)

@client.command(pass_context=True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
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
                                         																					
@client.command(pass_context=True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
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

	
@client.command(pass_context=True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def hug(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if user.id == ctx.message.author.id:
        await client.say("{} Wanted to hug himself/herself , good luck on that you will look like an idiot trying to do it".format(user.mention))
    else:
        randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)		
        
@client.command(description="Fetches a player's Fortnite stats.",no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
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
                     + "Number of matches: " + str(numMatches) + 
                     + "Top 10s: " + str(top10s) + "\n"
                     + "Top 5s: " + str(top5s)  
                     + "Top 3s: " + str(top3s) + "\n"
                     + "Wins: " + str(wins) + "\n"
                     + "Win percentage: " + str(winPct) + "\n"
                     + "Kills: " + str(kills) + "\n"
                     + "K/D: " + str(kd) + "\n")        


@client.command(pass_context=True,no_pm=True)
async def help(ctx):	
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title="Dot | My biggest project on Discord", description="", color = discord.Color((r << 16) + (g << 8) + b))			  
        embed.add_field(name="<a:8104LoadingEmote:535140498495766548> **Information:**", value="`help`, `info`, `ping`, `uptime`, `avatar`, `icon`", inline=False)
        embed.add_field(name=":closed_lock_with_key: **Developer Commands:**", value="`quit`, `emojiids`", inline=False)
        embed.add_field(name=":printer: **Internet Commands:**", value="`wiki`, `urban`", inline=False)	
        embed.add_field(name="<:FeelsHappyHugMan:535141367475863563> **Fun:**", value="`love`, `fortnite`, `penis`, `hug`, `kiss`, `howgay`, `rps`, `coinflip`", inline=False)
        embed.add_field(name=":cat: **Animals:**", value="`dog`, `cat`, `bird`, `duck`, `aww`", inline=False)    
        embed.add_field(name="<:2109_yikes:535142625129267231> **Memes:**", value="`meme`", inline=False)	
        embed.add_field(name=":underage: **NSFW:**", value="`hentai`, `butt`, `cosplay`", inline=False)
        embed.add_field(name="<:4206_lmaolancer2:535143040835125298> **Memes with Fun:**", value="`deepfry`, `text`, `czech`, `rotate`, `isthisa`, `phone`, `thatsmile`, `birthcontrol`, `moe`, `religion`, `disability`", inline=False)
        embed.add_field(name="<:1200pxFlag_of_the_Czech_Republic:535143419585232896> **Czech Commands:**", value="`8ball`, `vtip`, `fakt`, `svatek`, `zitra`", inline=False)
        embed.add_field(name="<:9175_moderation_hammer:535143648900284416> **Moderation:**", value="`ban`, `warn`, `say`, `purge`, `kick`, `unban`", inline=False)    
        embed.add_field(name=":musical_note: **Music:**", value="`play`, `stop`", inline=False)     
        embed.set_footer(text=f'Requested: {ctx.message.author.display_name} | Prefixes: [. or dot]', icon_url=f'{ctx.message.author.avatar_url}')
        await client.say(embed=embed)     
	
@client.command(pass_context = True,no_pm=True) 
async def hentai(ctx):
    colour = '0x' + '00ff1d'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/hentai/random") as r:
            data = await r.json()
            embed = discord.Embed(title='', description='', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)
					
@client.command(pass_context=True,no_pm=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def rps(ctx, *, message=None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    await client.send_typing(ctx.message.channel)
    ans = ["rock", "paper", "scissors"]
    pick=ans[random.randint(0, 2)]
    embed=discord.Embed(title = "Dot VS {}".format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    if message is None:
        await client.say('Use it like | Example: **.rps rock**')
    if message.lower() != ans[0] and message.lower() != ans[1] and message.lower() != ans[2] :
        return await client.say("<:joy:525410119199227915> | Please Only: Rock, Paper, Scissors!")
    elif message.lower() == pick:
        embed.add_field(name = "Its a draw!", value = "Dot picked {} too!".format(pick))
        return await client.say(embed=embed)
    else:
        if message.lower()  == "rock" and pick == "paper":
            embed.add_field(name = "Dot wins!", value = "Dot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "rock" and pick == "scissors":
            embed.add_field(name = "{} wins!".format(ctx.message.author.name), value = "Dot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "paper" and pick == "rock":
            embed.add_field(name = "{} wins!".format(ctx.message.author.name), value = "Dot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "paper" and pick == "scissors":
            embed.add_field(name = "Dot wins!", value = "Dot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "scissors" and pick == "rock":
            embed.add_field(name = "Dot wins!", value = "Dot picked {}!".format(pick))
            await client.say(embed=embed)
        else:
            embed.add_field(name = "{} wins!".format(ctx.message.author.name), value = "Dot picked {}!".format(pick))
            await client.say(embed=embed)

@client.command(pass_context = True,no_pm=True)
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def aww(ctx):
    colour = '0x' + '007000'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/aww/random") as r:
            data = await r.json()
            embed = discord.Embed(title='', description='', color=0x0000FF)
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)

@client.command(pass_context = True,no_pm=True)
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def cat(ctx):
    colour = '0x' + 'ff00d0'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/cat/random") as r:
            data = await r.json()
            embed = discord.Embed(title='', description='', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)


@client.command(pass_context = True,no_pm=True)
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def dog(ctx):
    colour = '0x' + '9dff00'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/dogpictures/random") as r:
            data = await r.json()
            embed = discord.Embed(title='', description='', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)	
	
		
@client.command(pass_context = True,no_pm=True)
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def duck(ctx):
    colour = '0x' + 'fce300'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/duck/random") as r:
            data = await r.json()
            embed = discord.Embed(title='', description='', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)		
	
	
@client.command(pass_context = True,no_pm=True)
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def bird(ctx):
    colour = '0x' + 'ff0059'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/birdpics/random") as r:
            data = await r.json()
            embed = discord.Embed(title='', description='', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.timestamp = datetime.datetime.utcnow()


@client.command(pass_context=True, no_pm=True)
async def icon(ctx):
    colour = '0x' + 'fce300'
    embed = discord.Embed(title='', description='', color=discord.Color(int(colour, base=16)))
    embed.set_image(url="{}".format(ctx.message.server.icon_url))
    await client.say(embed=embed)
							
client.run(TOKEN, client = True)
		                                                                                                
