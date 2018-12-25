import json
redditdata = json.load(open("config/reddit_data.json","r"))



import discord
import praw
import random
from discord.ext import commands


class NSFW:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("NSFW Cog was loaded successfully! ( ͡° ͜ʖ ͡°)")



    @commands.command(aliases=['Hentai'])
    async def hentai(self, ctx):
        if ctx.channel.is_nsfw() == False:
            await ctx.send("Sorry {}, you have to be in an NSFW channel to use that command!".format(ctx.message.author.mention))
        else:
            reddit = praw.Reddit(client_id=redditdata['clientid'],
                                 client_secret=redditdata['clientsecret'],
                                 user_agent=redditdata['useragent'])
            memes_submissions = reddit.subreddit('hentai').new()
            post_to_pick = random.randint(1, 10)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title=submission.title, color=0xc367ff, url=submission.shortlink)
            embed.set_image(url=submission.url)
            embed.set_footer(text='Straight from r/hentai!')

            await ctx.send(embed=embed)



    @commands.command(aliases=['Paizuri'])
    async def paizuri(self, ctx):
        if ctx.channel.is_nsfw() == False:
            await ctx.send("Sorry {}, you have to be in an NSFW channel to use that command!".format(ctx.message.author.mention))
        else:
            reddit = praw.Reddit(client_id=redditdata['clientid'],
                                 client_secret=redditdata['clientsecret'],
                                 user_agent=redditdata['useragent'])
            memes_submissions = reddit.subreddit('paizuri').hot()
            post_to_pick = random.randint(1, 10)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title=submission.title, color=0xc367ff, url=submission.shortlink)
            embed.set_image(url=submission.url)
            embed.set_footer(text='Straight from r/paizuri!')

            await ctx.send(embed=embed)




    @commands.command(aliases=['Neko'])
    async def neko(self, ctx):
        if ctx.channel.is_nsfw() == False:
            await ctx.send("Sorry {}, you have to be in an NSFW channel to use that command.".format(ctx.message.author.mention))
        else:
            reddit = praw.Reddit(client_id=redditdata['clientid'],
                                 client_secret=redditdata['clientsecret'],
                                 user_agent=redditdata['useragent'])
            memes_submissions = reddit.subreddit('nekogirls').hot()
            post_to_pick = random.randint(1, 10)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title=submission.title, color=0xc367ff, url=submission.shortlink)
            embed.set_image(url=submission.url)
            embed.set_footer(text='Straight from r/nekogirls!')

            await ctx.send(embed=embed)


    @commands.command()
    async def loli(self, ctx):
        if ctx.channel.is_nsfw() == False:
            await ctx.send("Sorry {}, you have to be in an NSFW channel to use that command.. Also I'm pretty sure that's pedophilia..".format(ctx.message.author.mention))

        else:
            fbi_memes = [
                discord.File('images/FBI/FBI.jpg'),
                discord.File('images/FBI/FBI2.png'),
                discord.File('images/FBI/FBI3.gif'),
                discord.File('images/FBI/FBI4.jpg'),
                discord.File('images/FBI/FBI5.jpg'),
		        discord.File('images/FBI/FBI6.gif')
            ]
            await ctx.send("**FBI OPEN UP!**\n", file=random.choice(fbi_memes))


def setup(bot):
    bot.add_cog(NSFW(bot))
