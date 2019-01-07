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

        await self.bot.send(embed=embed)
            
def setup(bot):
    bot.add_cog(info(bot))
