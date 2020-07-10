import discord
import json
from discord.ext import commands, tasks
from itertools import cycle

def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix, case_insensitive=True)
Bot = discord.client
client = bot
status = cycle(['Minecraft', '#Free Kekistan', '<prefix>help For Help'])

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



def setup(bot):
    bot.add_cog(Startup(bot))
    print('Startup Loaded')