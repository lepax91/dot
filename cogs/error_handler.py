import traceback
import sys
import discord
from discord.ext import commands
from discord import errors
"""
If you are not using this inside a cog, add the event decorator e.g:
@bot.event
async def on_command_error(ctx, error)
For examples of cogs see:
Rewrite:
https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
Async:
https://gist.github.com/leovoel/46cd89ed6a8f41fd09c5
This example uses @rewrite version of the lib. For the async version of the lib, simply swap the places of ctx, and error.
e.g: on_command_error(self, error, ctx)
For a list of exceptions:
http://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#errors
"""


class CommandErrorHandler:
	def __init__(self, bot):
		self.bot = bot
	async def on_command_error(self, error, ctx):
		channel = ctx.message.channel
		if isinstance(error,commands.CommandOnCooldown):
			return await self.bot.send_message(channel, f"Cool down {ctx.message.author.mention}, **{error.retry_after:.1f}** you must endure!")		
		elif isinstance(error,commands.NoPrivateMessage):
			return await self.bot.send_message(channel, f"You can't use command in **DM**!")
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
def setup(bot):
	bot.add_cog(CommandErrorHandler(bot))
