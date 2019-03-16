import json
import random
import vtipek
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
	@commands.command(pass_context = True,no_pm=True,aliases=['clean','delete','smaz','ocista'])
	@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
	@has_permissions(manage_messages=True)
	async def purge(self,ctx, number):	
		await self.bot.send_typing(ctx.message.channel)
		mgs = [] #Empty list to put all the messages in the log
		number = int(number) #Converting the amount of messages to delete to an integer
		if number > 100:
			return await self.bot.say(':x: | Oh, toto se mi nepodařilo udělat protože limit je 100.')						
		if number!=100:
			number+=1
		async for x in self.bot.logs_from(ctx.message.channel, limit = number):
			mgs.append(x)
		await self.bot.delete_messages(mgs)
		await self.bot.say(":put_litter_in_its_place: | Vyhodilo se x"+str(number-1))
		
	@commands.command(pass_context=True,no_pm=True)
	@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
	async def vtip(self,ctx):
		msg = vtipek.vtipek()
		await self.bot.say(""+msg+"")
	
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

	  										
												
	@commands.command(no_pm=True,Laliases=["zítra"])
	async def zitra(self):
		r = requests.get("https://api.abalin.net/get/tomorrow").json()
		svatek_cz = r["data"]["name_cz"]
		e=discord.Embed(title="Svátek", description=f"Zítra má svátek **{svatek_cz}**!", colour=random.randint(0, 0xFFFFFF))
		await self.bot.say(embed=e)

	@commands.group(pass_context= True,no_pm=True,aliases=["svátek"])
	@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
	async def svatek(self,ctx):
		if ctx.invoked_subcommand is None:
			r = requests.get("https://api.abalin.net/get/today").json()
			svatek_cz = r["data"]["name_cz"]
		        e=discord.Embed(title="Svátek", description=f"Dnes má svátek **{svatek_cz}**!", colour=random.randint(0, 0xFFFFFF))
		        await self.bot.say(embed=e)
					  
									
def setup(bot):
	bot.add_cog(Fun(bot))
