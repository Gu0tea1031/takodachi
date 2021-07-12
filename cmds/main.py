import discord 
from discord.ext import commands
from core.classes import Cog_extension 

class Main(Cog_extension):
    def __init__(selF,client):
        selF.client = client

    @commands.command()
    async def ping(selF,ctx):
      await ctx.send(f'{round(selF.client.latency*1000)}(ms)')

def setup(client):
    client.add_cog(Main(client))