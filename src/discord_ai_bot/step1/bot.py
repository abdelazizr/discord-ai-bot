import discord
import my_openai
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

    if message.content.startswith('$hello'):
        await message.channel.send('Hello, how can I help?')
    
# Check if the message starts with a question keyword
    if message.content.startswith('!ask'):
        # Remove the command part and strip leading/trailing whitespace
        user_question = message.content[len('!ask'):].strip()
        
        if user_question:
            
            try:
                response = my_openai.generate_answer(message.content)
                await message.channel.send("Hang Tight! Looking for the response...")
                await message.channel.send(response)
            
            except Exception as e:
                await message.channel.send(f"Error processing your request: {str(e)}")
        else:
            await message.channel.send("Please provide a question after !ask")


    if message.content.startswith('$question'):
        response = my_openai.generate_answer(message.content)
        await message.channel.send("looking for response")
        await message.channel.send(response)

    # elif message.content.startswith('!bye'):
    #     await message.channel.send('Goodbye!')

# Replace 'your_token_here' with your bot's actual token
client.run(os.environ["DISCORD_TOKEN"])

