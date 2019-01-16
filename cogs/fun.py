import json
import random
import vtipek
import discord
import requests
import eightballer
import urllib.request
from io import BytesIO
from bs4 import BeautifulSoup
from unidecode import unidecode
from discord.ext import commands
from discord.ext.commands import has_permissions

class Fun:
	def __init__(self,bot):
		self.bot = bot	
	@commands.command(pass_context = True,no_pm=True,aliases=['clean','delete','smaz','ocista'])
	@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
	@has_permissions(manage_messages=True)
	async def purge(self,ctx, number):	
		await self.bot.send_typing(ctx.message.channel)
		mgs = [] #Empty list to put all the messages in the log
		number = int(number) #Converting the amount of messages to delete to an integer
		if number > 100:
			return await self.bot.say('Limit is 100 message, just cool down.')
		if number!=100:
			number+=1
		async for x in self.bot.logs_from(ctx.message.channel, limit = number):
			mgs.append(x)
		await self.bot.delete_messages(mgs)
		await self.bot.say(":put_litter_in_its_place: x"+str(number-1))
	
	@commands.command(pass_context=True, aliases = ["8ball","magickakoule","choose"])
	@commands.cooldown(rate=1, per=2, type=commands.BucketType.user)
	async def eightball(self,ctx):
		msg = eightballer.eightball_pick()
		await self.bot.say(msg)
	@commands.command(pass_context=True)
	@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
	async def vtip(self,ctx):
		msg = vtipek.vtipek()
		await self.bot.say(""+msg+"")
	
	@commands.command(pass_context=True)
	@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
	async def fakt(self,ctx):
		url = "http://www.faktomat.cz/fakty/nahodne"
		r = urllib.request.urlopen(url)
		soup = BeautifulSoup(r,'html.parser')
		result = soup.find("div", {"class":"lead"}).text
		await self.bot.say(f"{result}")	

	@commands.command(pass_context = True)
	@commands.cooldown(rate=1, per=2, type=commands.BucketType.user)
	async def penis(self,ctx,user:discord.Member = None):
		if user is None:
			user = ctx.message.author
		e=discord.Embed(title="penis machine fam", colour=random.randint(0, 0xFFFFFF))
		e.add_field(name=f"{str(user)[:-5]}'s size",value="8"+'='*random.randrange(0,10)+"D")
		await self.bot.say(embed=e)
	
	@commands.group(pass_context= True)
	@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
	async def holiday(self,ctx):
		if ctx.invoked_subcommand is None:
			r = requests.get("https://api.abalin.net/get/today").json()
			svatek_cz = r["data"]["name_cz"]
			await self.bot.say(f"Today have got holiday: **{svatek_cz}**!")
		
def setup(bot):
	bot.add_cog(Fun(bot))
