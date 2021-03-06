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
				await self.bot.say(":warning: Toto číslo neexistuje, zadejte správné číslo.")
				return
		if factor == ():
			factor = 7.0
		try:
			im,filename=await self.getimage(ctx)
		except TypeError:
			return await self.bot.say(":warning: Tato fotka není ve velikostí jakou si já přeji.")
		im = im.convert(mode="RGB")
		im = ImageEnhance.Color(im).enhance(factor/2)
		im = ImageEnhance.Sharpness(im).enhance(factor*15)	
		im = ImageEnhance.Contrast(im).enhance(factor*1.5)					
		im.save(filename,"JPEG",quality = 4)
		await self.bot.send_file(ctx.message.channel,filename)
		os.remove(filename)		

	@commands.command(pass_context=True,aliases=['impact','impactmeme','impakt','memetext','txt'])
	@commands.cooldown(rate=1, per=15, type=commands.BucketType.user)
	async def text(self,ctx,*text):
		await self.bot.send_typing(ctx.message.channel)
		if text == ():
			await self.bot.say(":warning: Do tohoto příkazu, musíte zadat nějaký text.")
			return
		text = ' '.join(text)
		para = textwrap.wrap(text, width=15)
		try:
			im,filename=await self.getimage(ctx)
		except TypeError:
			return await self.bot.say("")

		width, height = im.size
		draw = ImageDraw.Draw(im)					
		fnt = ImageFont.truetype("./images/extras/impact.ttf", int(height/5))
		current_h, pad = 0,1					
		
		for line in para:
		    w, h = draw.textsize(line, font=fnt)
		    #x = (width - w) / 2
		    draw.text((((width - w) / 2)-2, current_h-2), line, font=fnt,fill="black")
		    draw.text((((width - w) / 2)+2, current_h-2), line, font=fnt,fill="black")
		    draw.text((((width - w) / 2)-2, current_h+2), line, font=fnt,fill="black")
		    draw.text((((width - w) / 2)+2, current_h+2), line, font=fnt,fill="black")
		    draw.text((((width - w) / 2),current_h), line, font=fnt, fill="white")
		    current_h += h + pad	
		im = im.convert(mode="RGB")
		im.save(filename,"JPEG",quality = 90)
		await self.bot.send_file(ctx.message.channel,filename)
		os.remove(filename)

	@commands.command(pass_context=True,aliases=['meme1','jetoto','isthis'])
	@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
	async def isthisa(self,ctx,*args):
		await self.bot.send_typing(ctx.message.channel)
		if args == ():
			await self.bot.say("🤦 | Musíš mi dát nějaký ten text.")
			return
		text = ' '.join(args)
		try:
			im,filename=await self.getimage(ctx)
		except TypeError:
			return await self.bot.say(":thinking: | Tento obrázek není podle mojí velikosti.")
		size=200,300

		im.thumbnail(size,Image.ANTIALIAS)
		background = Image.open("./images/extras/meme_template3.jpg").convert('RGBA')
		im=im.convert("RGBA")
		background.paste(im,(650,80),im)
		width,height=background.size
		fnt = ImageFont.truetype("./images/extras/arial.ttf", int(height/15))
		draw = ImageDraw.Draw(background)	
		tw,th=50,700
		draw.text((tw-2, th-2), text, font=fnt,fill="black")
		draw.text((tw+2, th-2), text, font=fnt,fill="black")
		draw.text((tw-2, th+2), text, font=fnt,fill="black")
		draw.text((tw+2, th+2), text, font=fnt,fill="black")
		draw.text((50,700),text, font=fnt,fill="white")
		background =background.convert(mode="RGB")
		background.save(filename,"JPEG",quality = 90)
		await self.bot.send_file(ctx.message.channel,filename)
		os.remove(filename)	
def setup(bot):
	bot.add_cog(Images(bot))
