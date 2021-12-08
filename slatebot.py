import discord #imports discord.py module, allowing use of their API.
import os #for loading discord token from .env file
from discord.ext import commands, tasks 
from dotenv import load_dotenv #for loading dsicord token from .env file

load_dotenv()
token=os.getenv('discord_token') #pulls the discord token from a .env file -- 

# For the bot to launch with this set up, you must have a .env file with the following, excluding quotations "discord_token=DiscordBotTokenGoesHere" 

client = commands.Bot(command_prefix='!', activity=discord.Game(name="Scrabble")) 

@client.command()
async def ping(ctx):
  await ctx.channel.send("pong")
    
client.run(token)

    
