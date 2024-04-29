import discord
import os

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

# Replace 'your_token_here' with your bot's actual token
client.run('MTIzMzQxNjY5NDQyNTQ1MjU1NA.G9OzTw.nK1LE2nY1lckjgk_KilZp0MmMBWNJAIzIFPFXw')
