import discord #imports discord.py module, allowing use of their API.
import os #for loading discord token from .env file
from discord.ext import commands, tasks 
from dotenv import load_dotenv #for loading dsicord token from .env file

load_dotenv()
token=os.getenv('discord_token') #pulls the discord token from a .env file -- 

# For the bot to launch with this set up, you must have a .env file with the following, excluding quotations "discord_token=DiscordBotTokenGoesHere" 

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)  #Makes the bot prefix. 

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!') #prints a confirmation in the terminal that it has connected to discord
    await client.change_presence(activity=discord.Game('Scrabble'))  #sets the bots discord presence, such as playing "Yahtzee". 
    
client.run(token)

    
