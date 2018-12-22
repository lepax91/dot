import discord
from discord.ext import commands
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class images():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rip(self, ctx, user:discord.Member = None):
        """Rip dat user"""
        user = user or ctx.author
        if user.id == 454285151531433984:
            await ctx.send("Dont rip meh!")
        else:
            img = Image.open("rip.png")
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("American Captain.otf", 100)
            draw.text((131, 399), f"{user.name}", (0, 0, 0), font=font)
            img.save(f'{user.id}.png')
            await ctx.send(file=discord.File(f'{user.id}.png'))

    @commands.command()
    async def achievement(self, ctx, *, text = None):
        """Write a achievement"""
        if text == None:
            embed=discord.Embed(description="**achievement <text>**",color=0x9b9dff)
            await ctx.send(embed=embed)
        else:
            img = Image.open("hqdefault.png")
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("Minecraft.ttf", 23)
            draw.text((90, 182), text, (255, 255, 255), font=font)
            img.save(f'{ctx.author.id}.png')
            await ctx.send(file=discord.File(f'{ctx.author.id}.png'))

    @commands.command(name="avatar", aliases=['av'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def avatar_command(self, ctx, *, member: discord.Member = None):
        '''Gets someones pfp'''
        member = member or ctx.author
        av = member.avatar_url
        if ".gif" in av:
            av += "&f=.gif"
        em = discord.Embed(title="Avatar", url=av, color=0x9b9dff)
        em.set_author(name=str(member), icon_url=av)
        em.set_image(url=av)
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(images(bot))
