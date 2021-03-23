import discord
from discord.ext import commands
import datetime
import requests
import random
from random import choice


class Entertainment(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot


        #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Entertainment Cog is on')

        #Commands

    @commands.command(aliases=['rfacts', 'random_facts'])
    async def randomfacts(self, ctx):
        rfact = [
            "There are about 1500 potentially active volcanoes worldwide, aside from the continuous belt of volcanoes on the ocean floor. About 500 of these have erupted in historical time. Many of these are located along the Pacific Rim in what is known as the 'Ring of Fire'.",
            "Though I have never clocked one of our cows (we raise beef cattle, not dairy) I would guess they could run up to 15 or 20 mph, though they would not run that fast for very long.",
            "There is no firm boundary where space begins. However the Kármán line, at an altitude of 100 km (62 mi) above sea level, is conventionally used as the start of outer space in space treaties and for aerospace records keeping.",
            "U.S. nuclear-powered submarines can go faster than 25 knots (nautical miles per hour) underwater, which is approximately 29 miles per hour or 46 kilometers per hour.",
            "The cobra is deaf to the snake charmer's pipe, but follows the visual cue of the moving pipe and it can sense the ground vibrations from the snake charmer's tapping. Sometimes, for the sake of safety, all the venom in cobra's teeth is removed.",
            "The circumference of Earth at the equator is about 24,902 miles (40,075 km), but from pole-to-pole — the meridional circumference — Earth is only 24,860 miles (40,008 km) around. This shape, caused by the flattening at the poles, is called an oblate spheroid.",
            "The thyroid gland regulates the body's metabolism, while parathyroid glands regulate calcium levels and have no effect on metabolism.",
            "First, put your two fists together, fingers touching. This is the size of your brain. It weighs about 3 pounds.",
            "A common year is 365 days = 8760 hours = 525600 minutes = 31536000 seconds. A leap year is 366 days = 8784 hours = 527040 minutes = 31622400 seconds.",
            "Fires can not burn in the oxygen-free vacuum of space, but guns can shoot. Modern ammunition contains its own oxidizer, a chemical that will trigger the explosion of gunpowder, and thus the firing of a bullet, wherever you are in the universe. No atmospheric oxygen required.",
            "Your ears pop in airplanes because the air high above the surface of Earth is less dense than air near the surface, because air near the surface has all the air above it pushing down. Your inner ear has air trapped in it and as the atmospheric pressure changes, it causes pressure on your ear drum.",
            "The left lung is slightly smaller than the right lung because 2/3 of the heart is located on the left side of the body. The left lung contains the cardiac notch, an indentation in the lung that surrounds the apex of the heart. Each lung consists of several distinct lobes.",
            "The river rises in the Black Forest Mountains of Germany and flows eastward into the Black Sea. The Danube River is an important international waterway, flowing through or forming a part of the borders of ten countries and through major cities such as Vienna, Bratislava, Budapest, and Belgrade.",
            "Hatcher calculated that his .30-caliber rifle bullets reached terminal velocity—the speed at which air resistance balances the accelerating force of gravity—at 300 feet per second. You might die from a bullet moving at that speed, but it is unlikely.",
            "The average new car or light-duty truck sold in the 2003 model year tipped the scales at 4,021 pounds, breaking the two-ton barrier for the first time since the mid-1970s, according to a report released by the Environmental Protection Agency last week.",
            "Based on landmass, Vatican City is the smallest country in the world, measuring just 0.2 square miles, almost 120 times smaller than the island of Manhattan. Situated on the western bank of the Tiber River, Vatican City's two-mile border is landlocked by Italy.",
            "The Nike clothing brand is named after the Greek goddess of victory. The winged goddess Nike sat at the side of Zeus. Her presence symbolized victory, and she was said to have presided over some of history's earliest battles.",
            "There are five types of bones in the human body: long, short, flat, irregular, and sesamoid.",
            "Barton was appointed Prime Minister by Governor General Lord Hopetoun on 1 January 1901. He resigned from the position as Prime Minister in September 1903, because of health concerns. He then became a High Court Judge, a post he held till his death on 7 January 1920.",
            "Most humans (say 70 percent to 95 percent) are right-handed, a minority (say 5 percent to 30 percent) are left-handed, and an indeterminate number of people are probably best described as ambidextrous."]

        value = random.randint(0, 0xffffff)
        embed = discord.Embed(

            colour=value,
            title="Did you know that"

        )
        embed.add_field(name=f"Fact: {random.choice(rfact)}", value="str8 factz right here", inline=False)

        await ctx.send(embed=embed)


    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['As I see it, yes.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Don’t count on it.',
                     'It is certain.',
                     'It is decidedly so.',
                     'Most likely.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Outlook good.',
                     'Reply hazy, try again',
                     'Signs point to yes.',
                     'Very doubtful.',
                     'Without a doubt.',
                     'Yes.',
                     'Yes – definitely.',
                     'You may rely on it.']


        value = random.randint(0, 0xffffff)
        embed = discord.Embed(

            colour=value,

        )
        embed.add_field(name=f'**Question:** {question}\n**Answer:** {random.choice(responses)}', value="hope you feel good with this answer.", inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    async def coinflip(self, ctx, *, toss):
        responses = ['Heads🤯',
                     'Tails🦨']

        value = random.randint(0, 0xffffff)
        embed = discord.Embed(

            colour=value,

        )
        embed.add_field(name=f'**User Side:** {toss}\n**Result:** {random.choice(responses)}', value="Someone is gonna go cry to mommy.", inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=["aboutuser", "about_user", "userinfo", "user_info", "whoisme"])
    async def whois(self, ctx, member: discord.Member = None):
        member = member if member else ctx.author
        embed = discord.Embed(

            colour=member.colour,
            timestamp=ctx.message.created_at

        )

        roles = [role for role in member.roles]

        lenroles = len(roles) - 1

        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="User Name", value=member.name, inline=False)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Account Created", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                        inline=False)
        embed.add_field(name="Member Joined", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                        inline=False)
        embed.add_field(name=f"Roles ({lenroles})",
                        value=" ".join([r.mention for r in member.roles if r != ctx.guild.default_role]), inline=False)
        embed.add_field(name="Top Role", value=member.top_role.mention, inline=False)
        embed.add_field(name="Bot?", value=member.bot, inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=["avatar", "useravatar", "userpfp", "profilepicture", "profile_picture"])
    async def pfp(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(
            title=f"{member}'s Profile Picture",
            colour=member.colour
        )
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    #errors

    @whois.error
    async def whois_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('No user mentioned.')

    @coinflip.error
    async def coinflip_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please select a side.')

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please ask a question.')


def setup(bot):
    bot.add_cog(Entertainment(bot))
    print('Entertainment Loaded')
