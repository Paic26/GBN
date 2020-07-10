import discord
import json
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import traceback
import os

def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix, case_insensitive=True)
Bot = discord.client
client = bot
status = cycle(['Minecraft', '#Free Kekistan', '<prefix>help For Help'])
client.remove_command('help')

class Startup(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

        #Events
    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print('Startup Cog is on')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel1 = discord.utils.get(member.guild.channels, name='rules')
        channel = discord.utils.get(member.guild.channels, name='welcome')
        await channel.send(f'Welcome {member.mention} \n Please fill out the form in {channel1.mention} to get started')
        role = discord.utils.get(member.guild.roles, name='Member')
        await member.add_roles(role)
        print(f'{member} has joined a server')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server')

    @tasks.loop(seconds=12.5)
    async def change_status(self):
        await self.bot.change_presence(activity=discord.Game(next(status)))

    @commands.command(name='reload', description="Reload all/one of the bots cogs!")
    @commands.is_owner()
    async def reload(self, ctx, cog=None):
        if not cog:
            # No cog, means we reload all cogs
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    color=0x808080,
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir("./cogs/"):
                    if ext.endswith(".py") and not ext.startswith("_"):
                        try:
                            self.bot.unload_extension(f"cogs.{ext[:-3]}")
                            self.bot.load_extension(f"cogs.{ext[:-3]}")
                            embed.add_field(
                                name=f"Reloaded: `{ext}`",
                                value='\uFEFF',
                                inline=False
                            )
                        except Exception as e:
                            embed.add_field(
                                name=f"Failed to reload: `{ext}`",
                                value=e,
                                inline=False
                            )
                        await asyncio.sleep(0.5)
                await ctx.send(embed=embed)
        else:
            # reload the specific cog
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    color=0x808080,
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog.lower()}.py"
                if not os.path.exists(f"./cogs/{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"Failed to reload: `{ext}`",
                        value="This cog does not exist.",
                        inline=False
                    )

                elif ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        self.bot.unload_extension(f"cogs.{ext[:-3]}")
                        self.bot.load_extension(f"cogs.{ext[:-3]}")
                        embed.add_field(
                            name=f"Reloaded: `{ext}`",
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception:
                        desired_trace = traceback.format_exc()
                        embed.add_field(
                            name=f"Failed to reload: `{ext}`",
                            value=desired_trace,
                            inline=False
                        )
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Startup(bot))
    print('Startup Loaded')