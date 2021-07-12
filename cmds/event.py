import discord 
from discord.ext import commands
from core.classes import Cog_extension
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class event(Cog_extension):
    # @client.event
    # async def on_member_join(member):
    #     channel = client.get_channel(int(jdata['welcome_channel']))
    #     await channel.send(f'{member}welcome!')

    # @client.event
    # async def on_member_remove(member):
    #     channel = client.get_channel(int(jdata['welcome_channel']))
    #     await channel.send(f'{member}leave :(')
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if str(message.channel) == "private" and message.content != "":
            await message.channel.purge(limit = 1 )

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content.startswith('!p ') and str(message.channel) == "驚嘆號批":
            await message.channel.send('good song')
        elif str(message.channel) == "驚嘆號批":
            await message.channel.purge(limit = 1)
    
def setup(client):
    client.add_cog(event(client))