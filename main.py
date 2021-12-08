import discord #imports discord.py module, allowing use of their API.
import os #for loading discord token from .env file
from dotenv import load_dotenv #for loading dsicord token from .env file

load_dotenv()
token=os.getenv('discord_token') #pulls the discord token from a .env file -- 

# For the bot to launch with this set up, you must have a .env file with the following, excluding quotations "discord_token=DiscordBotTokenGoesHere" 

intents = discord.Intents.default() # sets permissions
intents.members = True

