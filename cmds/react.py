import discord 
from discord.ext import commands
from core.classes import Cog_extension
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class react(Cog_extension):
    @commands.command()
    async def 猜拳(self,ctx):
        random_pic = random.choice((jdata['Pic']))
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)



def setup(client):
    client.add_cog(react(client))