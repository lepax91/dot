import traceback
import sys
import discord
from discord.ext import commands
from discord import errors

class CommandErrorHandler:
	def __init__(self, bot):
		self.bot = bot
	async def on_command_error(self, error, ctx):
		channel = ctx.message.channel
		if isinstance(error,commands.CommandOnCooldown):
			return await self.bot.send_message(channel, f"{ctx.message.author.mention} Big Smoke, It's me Carl, chill, chill! - {error.retry_after:.1f} Cool down!")
		elif isinstance(error,commands.CommandNotFound):
			return await self.bot.send_message(channel,"Eh? This command does not exist (type .help pls)")
		elif isinstance(error,commands.CommandNotFound):		
			return await self.bot.send_message(channel,"Hold up, You can no longer use commands in Private Chat!")
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
def setup(bot):
	bot.add_cog(CommandErrorHandler(bot))
