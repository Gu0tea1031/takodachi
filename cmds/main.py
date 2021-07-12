import discord 
from discord.ext import commands
from core.classes import Cog_extension 

class Main(Cog_extension):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def ping(self,ctx):
      await ctx.send(f'{round(self.client.latency*1000)}(ms)')

def setup(client):
    client.add_cog(Main(client))