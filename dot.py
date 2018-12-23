import discord
from discord.ext.commands import Bot
from discord.ext  import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio 
import platform
import colorsys
import os
import requests
import random
import json
import aiohttp
from urllib.request import urlopen, Request
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType
import datetime

start_time = time.time()
starttime2 = time.ctime(int(time.time()))

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
      embed.add_field(name = 'Invite Link',value ="[Here you are](https://discordapp.com/api/oauth2/authorize?
client_id=523787927113826305&permissions=8&scope=bot)")
      embed.add_field(name = 'Upvote me!',value ="[Here you are](https://discordbots.org/bot/523787927113826305/vote)")
      embed.add_field(name = '🇬 = General (Main Help) ',value ='Any Fun Commands are here.',inline = False)    
      embed.add_field(name =' 🇲 = Moderation (Mod Help)',value ='Any Moderation Commands are here.', inline = False)
      embed.add_field(name =' 🇳 = Not Safe to Work (NSFW Help)', value='Any NSFW commands are here.',inline = False)	      		
      dmmessage = await client.send_message(author,embed=embed)
      reaction1 = '🇬'  
      reaction2 = '🇲' 
      reaction3 = '🇳'     
     	
      await client.add_reaction(dmmessage, reaction1)
      await client.add_reaction(dmmessage, reaction2)
      await client.add_reaction(dmmessage, reaction3)
      await client.say('<:a_:524648895796740126> | What are you waiting for, just look at DMs..')
	
   
        
			
@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == 
