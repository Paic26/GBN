import discord
import json
import requests
from discord.ext import commands, tasks
import random
from random import choice
import datetime
from bs4 import BeautifulSoup as Soup

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'})
with open("./json/slap.json", "r") as f:
    src = json.load(f)

gif = []

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'})
with open("./json/pat.json", "r") as f:
    src2 = json.load(f)

gif = []

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'})
with open("./json/kiss.json", "r") as f:
    src3 = json.load(f)

gif = []

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'})
with open("./json/hug.json", "r") as f:
    src4 = json.load(f)

gif = []


Bot = discord.client


class Emotes(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

        # Events

    @commands.Cog.listener()
    async def on_ready(self):
        print('Emotes Cog is on')


    @commands.command()
    @commands.has_role("Admin")
    async def scrapeurl1(ctx, url):
        htm = s.get(url)
        soup = Soup(htm.text, "html.parser")
        for img in soup.findAll('img', attrs={'class': 'resp-media'}):
            if "data:image/" in str(img):
                gif.append(img['src'])
            else:
                src.append(img['src'])
        with open("./json/slap.json", "w") as f:
            json.dump(src, f)

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        value = random.randint(0, 0xffffff)
        meme = discord.Embed(
            colour=value,
            timestamp=datetime.datetime.utcnow(),
            title=f"{ctx.author.display_name} Slapped {member.display_name}"
        )
        meme.set_image(url=choice(src))
        meme.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=meme)

    @commands.command()
    @commands.has_role("Admin")
    async def scrapeurl2(ctx, url):
        htm = s.get(url)
        soup = Soup(htm.text, "html.parser")
        for img in soup.findAll('img', attrs={'class': 'resp-media'}):
            if "data:image/" in str(img):
                gif.append(img['src2'])
            else:
                src.append(img['src2'])
        with open("./json/pat.json", "w") as f:
            json.dump(src, f)

    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        value = random.randint(0, 0xffffff)
        meme = discord.Embed(
            colour=value,
            timestamp=datetime.datetime.utcnow(),
            title=f"{ctx.author.display_name} Patted {member.display_name}"
        )
        meme.set_image(url=choice(src2))
        meme.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=meme)



    @commands.command()
    @commands.has_role("Admin")
    async def scrapeurl3(ctx, url):
        htm = s.get(url)
        soup = Soup(htm.text, "html.parser")
        for img in soup.findAll('img', attrs={'class': 'resp-media'}):
            if "data:image/" in str(img):
                gif.append(img['src3'])
            else:
                src.append(img['src3'])
        with open("./json/kiss.json", "w") as f:
            json.dump(src, f)

    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        value = random.randint(0, 0xffffff)
        meme = discord.Embed(
            colour=value,
            timestamp=datetime.datetime.utcnow(),
            title=f"{ctx.author.display_name} Kissed {member.display_name}"
        )
        meme.set_image(url=choice(src3))
        meme.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=meme)


    @commands.command()
    @commands.has_role("Admin")
    async def scrapeurl4(ctx, url):
        htm = s.get(url)
        soup = Soup(htm.text, "html.parser")
        for img in soup.findAll('img', attrs={'class': 'resp-media'}):
            if "data:image/" in str(img):
                gif.append(img['src4'])
            else:
                src.append(img['src4'])
        with open("./json/hug.json", "w") as f:
            json.dump(src, f)

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        value = random.randint(0, 0xffffff)
        meme = discord.Embed(
            colour=value,
            timestamp=datetime.datetime.utcnow(),
            title=f"{ctx.author.display_name} Hugged {member.display_name}"
        )
        meme.set_image(url=choice(src4))
        meme.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=meme)


def setup(bot):
    bot.add_cog(Emotes(bot))
    print('Emotes Loaded')
