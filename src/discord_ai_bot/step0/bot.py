import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # do not let the bot respond to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    
    elif message.content.startswith('hi'):
        await message.channel.send('welcome!')

    elif message.content.startswith('!bye'):
        await message.channel.send('Goodbye!')

client.run(os.environ["DISCORD_TOKEN"])