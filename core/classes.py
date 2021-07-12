import discord 
from discord.ext import commands

class Cog_extension(commands.Cog):
    def __init__(self,client):
        self.client = client