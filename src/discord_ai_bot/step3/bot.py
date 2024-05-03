import discord
import my_openai as opai
import os
from discord.ext import commands
from replit import db
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
# Initialize the Discord bot
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command(help="Ask the user what kind of summary they are looking for.")
async def choose_article(ctx):
    # Retrieve the articles from the Replit database
    articles = db["articles"]
    # Create a message with options
    options = "\n".join([f"Send {idx+1} for {key.replace('-', ' ').title()}" for idx, key in enumerate(articles.keys())])
    prompt = "Please choose from the below list:\n" + options
    await ctx.send(prompt)

    # Check function to validate the user's choice
    def check(m):
        return m.author == ctx.author and m.content.isdigit() and 1 <= int(m.content) <= len(articles)

    try:
        # Wait for user response
        msg = await bot.wait_for('message', check=check, timeout=60.0)  # 60 seconds to reply
        choice = int(msg.content) - 1
        selected_key = list(articles.keys())[choice]
        selected_article = articles[selected_key]
        # You can add additional functionality here to summarize the article
        await ctx.send(f"You selected: {selected_key.replace('-', ' ').title()}\nURL: {selected_article}")
        await ctx.send("Please wait while I get you the summary...")
        await ctx.send(opai.generate_summary(selected_article))

    except Exception as e:
        await ctx.send('No valid input received or timeout reached. Please try again.')

@bot.command(help="Sends a welcome message with useful resources.")
async def new_member(ctx):
    articles = db["articles"]
    most_recent_article_key = list(articles.keys())[-1]  # Getting the most recent article key
    most_recent_article_url = articles[most_recent_article_key]  # Getting the URL

    # Welcome message and resources
    welcome_message = (
        f"Welcome to the server, {ctx.author.mention}! 🎉 Here are some resources you might find helpful:\n"
        f"1. Check out our latest article: {most_recent_article_url}\n"
        f"2. Visit our Ubuntu Hive website for more insights: https://dev.ubuntuhive.tech/en-us/\n"
        f"3. Learn more about tech with this comprehensive tutorial: [Insert Your Tutorial Link Here]\n"
        f"4. Other misc resources and info: [Insert More Links or Info Here]\n"
    )

    await ctx.send(welcome_message)

# Run the bot
token = os.getenv("DISCORD_TOKEN")
if token:
  bot.run(token)
else:
  print("Error: Discord token not found in environment variables. Please ensure DISCORD_TOKEN is set.")