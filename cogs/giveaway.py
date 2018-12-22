import discord
from discord.ext import commands
import asyncio, random, datetime

class start():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def start(self, ctx, duration,*, prize):
        """Start a giveaway!"""
        unit = duration[-1]
        if unit == 's':
            duration = int(duration[:-1])
            longunit = 'seconds'
            embed=discord.Embed(title="**Giveaway**", description=f"Prize: {prize} | Duration: {duration}", color=0xe156f1, timestamp = datetime.datetime.utcnow())
            embed.set_footer(text = "React with 🎉 to enter!")
            message = await ctx.send(embed=embed)
            await message.add_reaction("🎉")
            entries = []
            def check(reaction, user):
                return str(reaction.emoji) == "🎉" and user != self.bot.user
            for i in range(0, (duration*2) + 1):
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", check=check, timeout=0.5)
                    entries.append(user.id)
                except asyncio.TimeoutError:
                    pass
                if i == (duration*2) and len(entries) != 0:
                    winner = (f"<@{random.choice(entries)}>")
                    end=discord.Embed(title="**Giveaway ended**",description=f"""Winner: **{winner}**! You won **{prize}**!
🎉Participants: {len(entries)}""", color=0xc934da)
                    await message.edit(embed=end)
                    await ctx.send("Congratulations **{}**!".format(winner) + " You won **{}**!".format(prize))
                elif i == (duration*2) and len(entries) == 0:
                    no_winner= discord.Embed(title=prize, description="There was no winner", color=0xff0606, timestamp = datetime.datetime.utcnow())
                    no_winner.set_footer(text = "Ended")
                    await message.edit(embed=no_winner)
                    await ctx.send("**No winner was chosen!**")
        if unit == 'm':
            time = int(duration[:-1]) * 60
            longunit = 'minutes'
            embed=discord.Embed(title="**Giveaway**", description=f"Prize: {prize} | Duration: {duration}", color=0xe156f1, timestamp = datetime.datetime.utcnow())
            embed.set_footer(text = "React with 🎉 to enter!")
            message = await ctx.send(embed=embed)
            await message.add_reaction("🎉")
            entries = []
            def check1(reaction, user):
                return str(reaction.emoji) == "🎉" and user != self.bot.user
            for i in range(0, (time*2) + 1):
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", check=check1, timeout=0.5)
                    entries.append(user.id)
                except asyncio.TimeoutError:
                    pass
                if i == (time*2) and len(entries) != 0:
                    winner = (f"<@{random.choice(entries)}>")
                    end=discord.Embed(title="**Giveaway ended**",description=f"""Winner: **{winner}**! You won **{prize}**!
🎉Participants: {len(entries)}""", color=0xc934da)
                    await message.edit(embed=end)
                    await ctx.send("Congratulations **{}**!".format(winner) + " You won **{}**!".format(prize))
                elif i == (time*2) and len(entries) == 0:
                    no_winner= discord.Embed(title=prize, description="There was no winner", color=0xff0606, timestamp = datetime.datetime.utcnow())
                    no_winner.set_footer(text = "Ended")
                    await message.edit(embed=no_winner)
                    await ctx.send("**No winner was chosen!**")
                        
def setup(bot):
    bot.add_cog(start(bot))
