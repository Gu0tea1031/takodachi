import discord 
from discord.ext import commands
import json
import random
import os

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))
    channel = client.get_channel(int(jdata['channel']))
    await channel.send('tako online')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)}(ms)')

@client.command()
async def 猜拳(ctx):
    random_pic = random.choice((jdata['Pic']))
    pic = discord.File(random_pic)
    await ctx.send(file = pic)

client.run(jdata['TOKEN'])