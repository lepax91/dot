import os
import discord
import textwrap
import requests
import shutil
from discord.ext import commands
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
class Images:
	def __init__(self,bot):
		self.bot=bot
	async def getimage(self,ctx):
		async for x in self.bot.logs_from(ctx.message.channel, limit = 15):
			if x.attachments != []:
				suffixes = ('.jpeg','.jpg','.png')
				if x.attachments[0]['url'].endswith(suffixes):
					filename = x.attachments[0]['url'].split('/')
					filename = filename[-1]
					response = requests.get(x.attachments[0]['url'], stream=True)
					filename = ctx.message.server.id + filename
					with open(filename, 'wb') as out_file:
						shutil.copyfileobj(response.raw, out_file)
					size=500,500
					im = Image.open(filename)
					width,height = im.size
					if width > 2100 or height > 2100:
						#await self.bot.say("Obrázek je moc velký")
						im.close()
						os.remove(filename)
						del response
						return None
					im.thumbnail(size)
					del response
					return (im,filename)

	@commands.command(pass_context=True,aliases=['df','trojobal','obrazekvtrojobalu','deep-fry','deep_fry'])
	@commands.cooldown(rate=1, per=15, type=commands.BucketType.user)
	async def deepfry(self,ctx,*factor):
		await self.bot.send_typing(ctx.message.channel)
		if len(factor)>0 and len(factor)<2:
			try:
				factor=float(factor[0])
			except:
				await self.bot.say("To as není úplně číslo, co?")
				return
		if factor == ():
			factor = 7.0
		try:
			im,filename=await self.getimage(ctx)
		except TypeError:
			return await self.bot.say("No image of the correct size I could find :cry:)
		im = im.convert(mode="RGB")
		im = ImageEnhance.Color(im).enhance(factor/2)
		im = ImageEnhance.Sharpness(im).enhance(factor*15)	
		im = ImageEnhance.Contrast(im).enhance(factor*1.5)					
		im.save(filename,"JPEG",quality = 4)
		await self.bot.send_file(ctx.message.channel,filename)
		os.remove(filename)		


	
	
								
	
 
def setup(bot):
	bot.add_cog(Images(bot))
