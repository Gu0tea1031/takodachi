import discord 
from discord.ext import commands
from core.classes import Cog_extension
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_extension):
    @commands.command()
    async def 猜拳(selF,ctx):
        random_pic = random.choice((jdata['Pic']))
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

def setup(client):
    client.add_cog(React(client))