import discord 
from discord.ext import commands
import json
import random
import os

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))
    channel = client.get_channel(int(jdata['channel']))
    await channel.send('tako online')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        client.load_extension(f'cmds.{filename[:-3]}')

if __name__=="__main__":
    client.run(jdata['TOKEN'])