
import discord
from discord.ext import commands
import random, asyncio, aiohttp, os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class fun():
    def __init__(self, bot):
        self.bot = bot
	
    @commands.command()
    async def lenny(self, ctx):
        """( ͡° ͜ʖ ͡°)"""
        await ctx.send("( ͡° ͜ʖ ͡°)")

    @commands.command()
    async def face(self, ctx):
        """Get a face"""
        faces=["¯\_(ツ)_/¯", "̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\З= ( ▀ ͜͞ʖ▀) =Ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿", "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)", "ʕ•ᴥ•ʔ", "(▀̿Ĺ̯▀̿ ̿)", "(ง ͠° ͟ل͜ ͡°)ง", "༼ つ ◕_◕ ༽つ", "ಠ_ಠ", "(づ｡◕‿‿◕｡)づ", "̿'̿'\̵͇̿̿\З=( ͠° ͟ʖ ͡°)=Ε/̵͇̿̿/'̿̿ ̿ ̿ ̿ ̿ ̿", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)", "┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴", "( ͡°╭͜ʖ╮͡° )", "(͡ ͡° ͜ つ ͡͡°)", "(• ε •)", "(ง'̀-'́)ง", "(ಥ﹏ಥ)", "(ノಠ益ಠ)ノ彡┻━┻", "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "(☞ﾟ∀ﾟ)☞", "| (• ◡•)| (❍ᴥ❍ʋ)", "(◕‿◕✿)", "(ᵔᴥᵔ)", "(¬‿¬)", "(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)", "(づ￣ ³￣)づ", "ლ(ಠ益ಠლ)", "ಠ╭╮ಠ", "̿ ̿ ̿'̿'\̵͇̿̿\з=(•_•)=ε/̵͇̿̿/'̿'̿ ̿", "(;´༎ຶД༎ຶ`)", "༼ つ  ͡° ͜ʖ ͡° ༽つ", "(╯°□°）╯︵ ┻━┻"]
        face=random.choice(faces)
        await ctx.send(face)

    @commands.command()
    async def tableflip(self, ctx):
        """Flip da table"""
        x = await ctx.send(content="┬─┬ノ( º _ ºノ)")
        await asyncio.sleep(1)
        await x.edit(content='(°-°)\\ ┬─┬')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯    ]')
        await asyncio.sleep(0.2)
        await x.edit(content='(╯°□°)╯  ︵  ┻━┻')

    @commands.command()
    async def roast(self, ctx, user: discord.Member):
        """Roast @someone"""
        roasts = ["your ass must be pretty jealous of all the shit that comes out of your mouth.","some day you'll go far, and I hope you stay there.","I'm trying my absolute hardest to see things from your perspective, but I just can't get my head that far up my ass.","I'm not a protocolgist, but I know an asshole when I see one.","Do yourself a favor and ignore anyone who tels you to be yourself. Bad idea in your case.","Everyone's entitled to act stupid once in awhile, but you really abuse the privilege.","Can you die of constipation? I ask because I'm worried about how full of shit you are.","Sorry, I didn't get that. I don't speak bullshit.","There are some remarkably dumb people in this world. Thanks for helping me understand that.","I could eat a bowl of alphabet soup and shit out a smarter statement than whatever you just said.","You always bring me so much joy, as soon as you leave the room.","I'd tell you how I really feel, but I wasn't born with enough middle fingers to express myself in this case.","You have the right to remain silent because whatever you say will probably be stupid anyway.","your family tree must be a cactuss because you're all a bunch of pricks.","You'll never be the man your mom is.","If laughter is the best medicine, your face must be curing the world.","scientists say the universe is made up of neutrons, protons and electrons. They forgot to mention morons, as you are one.","if you really want to know about mistakes, you should ask your parents.","I thought of you today. It reminded me to take the garbage out.","you're such a beautiful, intelligent, wonderful person. Oh I'm sorry, I thought we were having a lying competition.","I may love to shop but I'm not buying your bullshit.","I just stepped in something that was smarter than you, and smelled better too."]
        roast = random.choice(roasts)
        if user.id == 454285151531433984:
            await ctx.send(f"**{ctx.author.name}** I aint going to roast myself faggot!")
        else:
            await ctx.send("**{}** | {}".format(user.name, roast)) 
         
		
    @commands.command()
    async def meme(self, ctx):
        """Get a amazing meme"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.reddit.com/r/me_irl/random") as r:
                data = await r.json()
                await ctx.send(data[0]["data"]["children"][0]["data"]["url"])				

    @commands.command()
    async def alia(self, ctx):
        await ctx.send("**Alia intro bass boosted**\nhttps://www.youtube.com/watch?v=170Wg6PyhnI")
		
    @commands.command()
    async def anthem(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=KjVLZLsW0do")		
		
    @commands.command()
    async def weeb(self, ctx):
        weeb = self.bot.get_user(277981712989028353)
        await ctx.send(f"{weeb.mention}")		
		
    @commands.command()
    async def freenitro(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    #@commands.command()
    #async def tweet(self, ctx,*,text):
        #if len(text) >= 27:
            #return await ctx.send("Message is to long, maximum 27 letters")
        #img = Image.open("tweet.png")
        #draw = ImageDraw.Draw(img)
        #font = ImageFont.truetype("LiberationSans.ttf", 75)
        #draw.text((50, 190), f"{text}",(0, 0, 0), font=font)
        #img.save(f"{ctx.author.id}.png")
        #await ctx.send(file=discord.File(f'{ctx.author.id}.png'))
	
    @commands.command()
    async def bongocat(self, ctx):
        await ctx.send(file=discord.File('bongo.gif'))	
	
#    @commands.command()
#    async def legends(self,ctx,*,text):
#        headers = {
#            "Authorization": os.environ.get('BANANA').strip('"')  # Replace with your actual token that you received.
#        }
#        params = {
#            "text": f"{text}" # Self-explanatory.
#        }
#        res = await self.bot.session.get("https://bananapi.ml/api/legends", headers=headers, params=params) # do the request
#        res = await res.read()
#	    await ctx.send(file=discord.File(res, "e.jpg"))
    
    @commands.command()
    async def tweet(self,ctx,*,text):
        """Makes trump tweet something"""
        params = {"text": f"{text}"}
        headers = {"Authorization": f"{os.environ.get('VILGOTAPI')}"}
        res = await self.bot.session.get("https://vilgotapi.glitch.me/api/trumptweet", headers=headers, params=params)
        res = await res.read()
        await ctx.send(file=discord.File(res, 'trumptweet.png'))

    @commands.command()
    async def facts(self,ctx,*,text):
        """Your own facts"""
        params = {"text": f"{text}"}
        headers = {"Authorization": f"{os.environ.get('VILGOTAPI')}"}
        res = await self.bot.session.get("https://vilgotapi.glitch.me/api/facts", headers=headers, params=params)
        res = await res.read()
        await ctx.send(file=discord.File(res, 'facts.png'))
    @commands.command()
    async def alert(self,ctx,*,text):
        """PRESIDENT ALERT"""
        params = {"text": f"{text}"}
        headers = {"Authorization": f"{os.environ.get('VILGOTAPI')}"}
        res = await self.bot.session.get("https://vilgotapi.glitch.me/api/alert", headers=headers, params=params)
        res = await res.read()
        await ctx.send(file=discord.File(res, 'alert.png'))

    @commands.command()
    async def lmgtfy(self,ctx,*,text):
        txt = text.replace(" ","%20")
        await ctx.send(f"http://lmgtfy.com/?q={txt}")
		   
def setup(bot):
    bot.add_cog(fun(bot))
