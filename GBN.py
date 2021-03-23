import discord
import json
from discord.ext import commands
import  os
import asyncio
import datetime
from datetime import datetime
import random
import praw

with open('./json/config.json') as config:
    config_data = json.load(config)

bot = commands.Bot(command_prefix ="_",  case_insensitive=True, owner_id=382947478422421516)
Bot = discord.client
client = bot
client.remove_command('help')


bot.reddit = praw.Reddit(client_id=config_data['reddit_client_id'],
                          client_secret=config_data['reddit_client_secret'],
                          user_agent=config_data['reddit_user_agent'])

#cogs
@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded')



for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension((f'cogs.{filename[:-3]}'))



@bot.event
async def on_ready():
    print('Generic Bot Name Bot is ready \n-----------------------------')




@bot.command(aliases=["quit", "kill"])
@commands.is_owner()
async def shutdown(ctx):
    value = random.randint(0, 0xffffff)
    kill = discord.Embed(
        colour=value,
        title='GBN is now turned off!'
    )
    kill.set_footer(text=f"Shutdowned By {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=kill)
    await asyncio.sleep(2)
    await bot.close()


bot.run('NzA5NDQyNTcyNzc0NTM5Mjk0.Xrl94g.1ihxmRiyIAB04n3WomEyowyWJVQ')
