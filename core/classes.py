import discord 
from discord.ext import commands

class Cog_extension(commands.Cog):
    def __init__(selF,client):
        selF.client = client