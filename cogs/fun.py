import json
import random
import discord
import requests
import urllib.request
from io import BytesIO
from bs4 import BeautifulSoup
from unidecode import unidecode
from discord.ext import commands
from discord.ext.commands import has_permissions

class Fun:
	def __init__(self,bot):
		self.bot = bot	
			
	@commands.command(pass_context=True,no_pm=True)
	@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
	async def fakt(self,ctx):
		url = "http://www.faktomat.cz/fakty/nahodne"
		r = urllib.request.urlopen(url)
		soup = BeautifulSoup(r,'html.parser')
		result = soup.find("div", {"class":"lead"}).text
		e=discord.Embed(title=f"{result}", colour=random.randint(0, 0xFFFFFF))	
		await self.bot.say(embed=e)
		
	@commands.command(pass_context = True,no_pm=True)
	@commands.cooldown(rate=1, per=2, type=commands.BucketType.user)
	async def penis(self,ctx,user:discord.Member = None):
		if user is None:
			user = ctx.message.author
		e=discord.Embed(title="tenhle muž/žena má velký péro", colour=random.randint(0, 0xFFFFFF))
		e.add_field(name=f"{str(user)[:-5]} velikost péra",value="8"+'='*random.randrange(0,10)+"D")
		await self.bot.say(embed=e)

	

																			  									
def setup(bot):
	bot.add_cog(Fun(bot))
