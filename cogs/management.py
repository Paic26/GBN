import discord
from discord.ext import commands
import random
import datetime
from datetime import datetime
import platform

bot = commands.Bot(command_prefix="_", case_insensitive=True)
Bot = discord.client
client = bot
client.remove_command('help')
bot.launch_time = datetime.utcnow()

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
        embed.add_field(name="Check out all the commands", value="[Website Link](https://paic26.github.io/GenericBotWebsite)")
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

    @commands.command(aliases=["pm"])
    async def dm(self, ctx, member: discord.Member, *, text):
        await ctx.message.delete()
        await member.send(f"{ctx.author} sent this dm:\n\n {text}")
        print(f"{ctx.author} DMed {member}: {text}")        

    @commands.command(name='serverinfo', pass_context=True)
    async def serverinfo(self, context):
            server = context.message.guild
            roles = [x.name for x in server.roles]
            role_length = len(roles)
            if role_length > 50:
                roles = roles[:50]
                roles.append('>>>> Displaying[50/%s] Roles' % len(roles))
            roles = ', '.join(roles)
            channelz = len(server.channels)
            time = str(server.created_at)
            time = time.split(' ')
            time = time[0]
            embed = discord.Embed(description='%s ' % (str(server)), title='**Server Name:**', color=0x00FF00)
            embed.set_thumbnail(url=server.icon_url)
            embed.add_field(name='__Owner__', value=str(server.owner) + '\n' + str(server.owner.id))
            embed.add_field(name='__Server ID__', value=str(server.id))
            embed.add_field(name='__Member Count__', value=str(server.member_count))
            embed.add_field(name='__Text/Voice Channels__', value=str(channelz))
            embed.add_field(name='__Roles (%s)__' % str(role_length), value=roles)
            embed.set_footer(text='Created at: %s' % time)
            await context.message.channel.send(embed=embed)

    @commands.command(pass_context=True)
    async def poll(self, ctx, *args):
        mesg = ' '.join(args)
        await ctx.message.delete()
        embed = discord.Embed(title='We have a poll !',
                              description='{0}'.format(mesg),
                              color=0x00FF00)

        embed.set_footer(text='Poll created by: {0} • React to vote!'.format(ctx.message.author))

        embed_message = await ctx.send(embed=embed)

        await embed_message.add_reaction('👍')
        await embed_message.add_reaction('👎')
        await embed_message.add_reaction('🤷')

    @commands.command()
    async def uptime(self, ctx):
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

    @commands.command()
    async def stats(self, ctx):

        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))

        embed = discord.Embed(title=f'{self.bot.user.name} Stats',
                              description='\uFEFF',
                              colour=ctx.author.colour,
                              timestamp=ctx.message.created_at)

        embed.add_field(name='Bot Version:', value="2.7", inline=False)
        embed.add_field(name='Python Version:', value=f"{pythonVersion}", inline=False)
        embed.add_field(name='Discord.Py Version', value=f"{dpyVersion}", inline=False)
        embed.add_field(name='Total Guilds:', value=f"{serverCount}", inline=False)
        embed.add_field(name='Total Users:', value=f"{memberCount}", inline=False)
        embed.add_field(name='Bot Developers:', value="<@382947478422421516>")

        embed.set_footer(text=f"Yours truly, | {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Management(bot))
    print('Management Loaded')
