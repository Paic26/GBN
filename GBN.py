import discord
import json
from discord.ext import commands
import  os
import asyncio
import datetime
from datetime import datetime
import random
import praw
import platform


def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

with open('./json/config.json') as config:
    config_data = json.load(config)

bot = commands.Bot(command_prefix = get_prefix,  case_insensitive=True, owner_id=382947478422421516)
Bot = discord.client
client = bot
client.remove_command('help')
bot.launch_time = datetime.utcnow()

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

bot.version='2.5'

for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension((f'cogs.{filename[:-3]}'))



@bot.event
async def on_ready():
    print('Generic Bot Name Bot is ready \n-----------------------------')

#Costumizable Prefixes

@client.event
async def on_guild_join(guild):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '_'

    with open('./json/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('./json/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


#stop the bot

@bot.command(aliases=["quit", "kill"])
@commands.is_owner()
async def shutdown(ctx):
    value = random.randint(0, 0xffffff)
    kill = discord.Embed(
        colour=value,
        timestamp=datetime.datetime.utcnow(),
        title='GBN is now turned off!'
    )
    kill.set_footer(text=f"Shutdowned By {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=kill)
    await asyncio.sleep(2)
    await bot.close()

@bot.command()
async def stats(ctx):

    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(bot.guilds)
    memberCount = len(set(bot.get_all_members()))

    embed = discord.Embed(title=f'{bot.user.name} Stats',
                          description='\uFEFF',
                          colour=ctx.author.colour,
                          timestamp=ctx.message.created_at)

    embed.add_field(name='Bot Version:', value=f"{bot.version}", inline=False)
    embed.add_field(name='Python Version:', value=f"{pythonVersion}", inline=False)
    embed.add_field(name='Discord.Py Version', value=f"{dpyVersion}", inline=False)
    embed.add_field(name='Total Guilds:', value=f"{serverCount}", inline=False)
    embed.add_field(name='Total Users:', value=f"{memberCount}", inline=False)
    embed.add_field(name='Bot Developers:', value="<@382947478422421516>")

    embed.set_footer(text=f"Yours truly, | {bot.user.name}")
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    value = random.randint(0, 0xffffff)
    up = discord.Embed(
        colour=value,
        title="Uptime",
        description="I've been online for:",
        timestamp=datetime.utcnow()
    )
    up.add_field(name=f"{days}d, {hours}h, {minutes}m, {seconds}s", value="\u200b", inline=False)
    await ctx.send(embed=up)
    
@bot.command(pass_context=True)
async def poll(context, *args):
	mesg = ' '.join(args)
	await message.delete()
	embed = discord.Embed(title='We have a poll !', description='{0}'.format(mesg), color=0x00FF00)
	embed.set_footer(text='Poll created by: {0} • React to vote!'.format(context.message.author))
	embed_message = await context.message.channel.send(embed=embed)
	await embed_message.add_reaction( '👍')
	await embed_message.add_reaction('👎')
	await embed_message.add_reaction('🤷')
        
        
bot.run(os.environ['DISCORD_TOKEN'])
