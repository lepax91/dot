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
        #RAM = psutil.virtual_memory()
        #used = RAM.used >> 30
        #percent = RAM.percent
        embed=discord.Embed(title=f"{self.bot.user.name} stats", color=0x9b9dff)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Uptime", value="**%dd %dh %dm %ds**"% (day, hour, minute, second), inline=False)
        embed.add_field(name="Servers", value=f"Servers: **{len(self.bot.guilds)}**", inline=False)
        embed.add_field(name="Users", value=str(len(self.bot.users)))
        #embed.add_field(name="Memory used", value=f"{used}GB ({percent}%)", inline=False)

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
            
#    @commands.command(name="translate", aliases=['tr'])
#    @commands.cooldown(1, 3, commands.BucketType.user)
#    async def translate_command(self, ctx, tl, *words: str):
#        '''Translate something. Supported list of languages: https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#languages
#        Usage: translate <from>-<to>
#        Example: translate en-pl sandwich
#        '''
#        words = ' '.join(words)
#        answer = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170315T092303Z.ece41a1716ebea56.a289d8de3dc45f8ed21e3be5b2ab96e378f684fa&text={0}&lang={1}".format(words,tl)).json()
#        await ctx.send("{0} {1}".format(ctx.message.author.mention, str(answer["text"])[2:-2]))            
            
def setup(bot):
    bot.add_cog(info(bot))
