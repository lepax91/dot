import discord
import requests
from discord.ext import commands
import json

class Wiki:
	def __init__(self,bot):
		self.bot = bot
	def cleanhtml(self,raw_html):
		cleanr = re.compile('<.*?>')
		cleantext = re.sub(cleanr, '', raw_html)
		return cleantext
	@commands.command(pass_context = True, aliases=['wikipedia','wikisearch','wikipedie'])
	async def wiki(self,ctx,*args):
		url="https://en.wikipedia.org/w/api.php?"
		if args == ():
			await self.bot.say(":x: | Chyba musíš použít příkaz jen takhle: `.wiki <slovo>`")					
		params = {
		'format':'json',
		'action':'query',
		'prop':'extracts',
		'exchars':500,
		'explaintext':True,
		'redirects': True,
		}
		o = ' '.join(args)
		args = '+'.join(args)
		newurl = url +"titles="+args
		try:
			r = requests.Session().get(url=newurl,params = params)
			data = r.json()
			data=data['query']['pages'].popitem()
			e = discord.Embed(colour = discord.Colour.blue())
			e.add_field(name=data[1]['title'],value=data[1]['extract'])
			await self.bot.say(embed = e),
		except KeyError:
			await self.bot.say(f":x: | Není vyhledáno protože ve Wikipedii toto slovo neexistuje.")
			return
def setup(bot):
	bot.add_cog(Wiki(bot))
