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

	def do_magik(self, scale, *imgs):
		try:
			list_imgs = []
			exif = {}
			exif_msg = ''
			count = 0
			for img in imgs:
				i = wand.image.Image(file=img)
				i.format = 'jpg'
				i.alpha_channel = True
				if i.size >= (3000, 3000):
					return ':warning: `Image exceeds maximum resolution >= (3000, 3000).`', None
				exif.update({count:(k[5:], v) for k, v in i.metadata.items() if k.startswith('exif:')})
				count += 1
				i.transform(resize='800x800>')
				i.liquid_rescale(width=int(i.width * 0.5), height=int(i.height * 0.5), delta_x=int(0.5 * scale) if scale else 1, rigidity=0)
				i.liquid_rescale(width=int(i.width * 1.5), height=int(i.height * 1.5), delta_x=scale if scale else 2, rigidity=0)
				magikd = BytesIO()
				i.save(file=magikd)
				magikd.seek(0)
				list_imgs.append(magikd)
			if len(list_imgs) > 1:
				imgs = [PIL.Image.open(i).convert('RGBA') for i in list_imgs]
				min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
				imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))
				imgs_comb = PIL.Image.fromarray(imgs_comb)
				ya = BytesIO()
				imgs_comb.save(ya, 'png')
				ya.seek(0)
			elif not len(list_imgs):
				return ':warning: **Command download function failed...**', None
			else:
				ya = list_imgs[0]
			for x in exif:
				if len(exif[x]) >= 2000:
					continue
				exif_msg += '**Exif data for image #{0}**\n'.format(str(x+1))+code.format(exif[x])
			else:
				if len(exif_msg) == 0:
					exif_msg = None
			return ya, exif_msg
		except Exception as e:
			return str(e), None

	@commands.command(pass_context=True, aliases=['imagemagic', 'imagemagick', 'magic', 'magick', 'cas', 'liquid'])
	@commands.cooldown(2, 5, commands.BucketType.user)
	async def magik(self, ctx, *urls:str):
		"""Apply magik to Image(s)\n .magik image_url or .magik image_url image_url_2"""
		try:
			get_images = await self.get_images(ctx, urls=urls, limit=6, scale=5)
			if not get_images:
				return
			img_urls = get_images[0]
			scale = get_images[1]
			scale_msg = get_images[2]
			if scale_msg is None:
				scale_msg = ''
			msg = await self.bot.send_message(ctx.message.channel, "ok, processing")
			list_imgs = []
			for url in img_urls:
				b = await self.bytes_download(url)
				if b is False:
					if len(img_urls) > 1:
						await self.bot.say(':warning: **Command download function failed...**')
						return
					continue
				list_imgs.append(b)
			final, content_msg = await self.bot.loop.run_in_executor(None, self.do_magik, scale, *list_imgs)
			if type(final) == str:
				await self.bot.say(final)
				return
			if content_msg is None:
				content_msg = scale_msg
			else:
				content_msg = scale_msg+content_msg
			await self.bot.delete_message(msg)
			await self.bot.upload(final, filename='magik.png', content=content_msg)
		except discord.errors.Forbidden:
			await self.bot.say(":warning: **I do not have permission to send files!**")
		except Exception as e:
			await self.bot.say(e)  										
																		  									
def setup(bot):
	bot.add_cog(Fun(bot))
