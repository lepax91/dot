import discord
from discord.ext import commands
import datetime, time, psutil

start_time = time.time()
starttime2 = time.ctime(int(time.time()))

class info():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx):
        """Get some stats about the bot"""
        second = time.time() - start_time
        minute, second = divmod(second, 60)
        hour, minute = divmod(minute, 60)
        day, hour = divmod(hour, 24)
        RAM = psutil.virtual_memory()
        used = RAM.used >> 30
        percent = RAM.percent
        embed=discord.Embed(title=f"{self.bot.user.name} stats", color=0x9b9dff)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Uptime", value="**%dd %dh %dm %ds**"% (day, hour, minute, second), inline=False)
        embed.add_field(name="Servers", value=f"Servers: **{len(self.bot.guilds)}**", inline=False)
        embed.add_field(name="Users", value=str(len(self.bot.users)))
        embed.add_field(name="Memory used", value=f"{used}GB ({percent}%)", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        """"Invite me"""
        embed=discord.Embed(description="**Invite me or join my support guild! And vote!**\n[Invite](https://discordapp.com/oauth2/authorize?client_id=454285151531433984&permissions=8&scope=bot)\n[Support guild](https://discord.gg/Z6d8Ecq)\n[Vote](https://discordbots.org/bot/454285151531433984/vote)", color=0x9b9dff)
        await ctx.send(embed=embed)
 
    @commands.command()
    async def suggest(self, ctx,*,suggestion=None):
        """Give a suggestion to me"""
        if suggestion==None:
            return await ctx.send("❌ | You need to add a suggestion")
        embed=discord.Embed(description=suggestion,color=0x00ff80, timestamp = datetime.datetime.utcnow())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"From {ctx.author.guild}")
        xd = self.bot.get_channel(457623659369070642)
        x = await xd.send(embed=embed)
        await x.add_reaction("✅")
        await x.add_reaction("❌")
        await ctx.send("✅ | Your suggestion has been made! kthx")
            
def setup(bot):
    bot.add_cog(info(bot))
