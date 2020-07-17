import discord
import json
from discord.ext import commands, tasks
import random
import datetime


def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
Bot = discord.client
client = bot
client.remove_command('help')


class Management(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

        # Events

    @commands.Cog.listener()
    async def on_ready(self):
        print('Management Cog is on')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        random.randint(0, 0xffffff)
        if isinstance(error, commands.CommandNotFound):
            value = random.randint(0, 0xffffff)
            embed = discord.Embed(
                colour=value,
                title="Command non-existent or broken."
            )
            embed.add_field(name="Do <prefix>help", value="for the available commands")
            await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(

            colour=discord.Colour.purple(),
            title="Invite the Bot!"
        )
        embed.add_field(name="Bot Invite", value="[Bot Invite Link](https://bit.ly/3dBozNZ)")
        await ctx.send(embed=embed)

    @commands.command(aliases=['source_code', 'source'])
    async def sourcecode(self, ctx):
        embed = discord.Embed(

            colour=discord.Colour.purple(),
            title="Bot Source Code!"
        )
        embed.add_field(name="For everyone to use", value="[Github](https://github.com/Paic26/GenericBotName/)")
        await ctx.send(embed=embed)

    
    @commands.command(aliases=["supportserver", "support_server", "help_server", "helpserver"])
    async def support(self, ctx):
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(

            colour=value,
            title="Join our support server!"
        )
        embed.add_field(name="Support Server", value="[Invite Link](https://discord.io/GenericBotName)")
        await ctx.send(embed=embed)

    @commands.command()
    async def website(self, ctx):
        embed = discord.Embed(

            colour=discord.Colour.purple(),
            title="Website"
        )
        embed.add_field(name="website in development", value="[Website Link]()")
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):

        value = random.randint(0, 0xffffff)
        embed = discord.Embed(

            colour=value,
            title=":ping_pong: Pong:ping_pong: "
        )
        embed.add_field(name=f'Ponged! {round(self.bot.latency * 1000)}ms', value=":ping_pong: Pong:ping_pong:")
        await ctx.send(embed=embed)

    @commands.command()
    async def check(self, ctx):
        await ctx.send('All good officer, 👮')

    @commands.command(aliases=['prefix'])
    async def change_prefix(self, ctx, prefix):
        with open('./prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: {prefix}')
        
        
    @commands.command(aliases=["pm"])
    async def dm(self, ctx, member: discord.Member, *, text):
        await ctx.message.delete()
        await member.send(f"{ctx.author} sent this dm:\n\n {text}")
        print(f"{ctx.author} DMed {member}: {text}")        

        
        
def setup(bot):
    bot.add_cog(Management(bot))
    print('Management Loaded')
