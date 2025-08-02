import discord
from discord.ext import commands
import requests
import random
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')

intents=discord.Intents.default()
intents.message_content=True

bot=commands.Bot(command_prefix='$',intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
@bot.command()
async def meme(ctx):
    try:
        res = requests.get("https://meme-api.com/gimme/memes+dankmemes+me_irl", timeout=10)
        data = res.json()
        meme_url = data['url']
        meme_title = data['title']
        meme_post_link = data['postLink']
        await ctx.send(f"**{meme_title}**\n{meme_url}\n<{meme_post_link}>")
    except Exception as e:
        print("Error fetching meme:", e)
        await ctx.send("Couldn't fetch a meme 😢 Try again later.")
@bot.command()
async def inspire(ctx):
    try:
        headers={"user-agent":"inspirebot"}
        res=requests.get("https://api.realinspire.live/v1/quotes/random", timeout=10)
        data=res.json()
        quote=data[0]['content']
        author=data[0]['author']
        await ctx.send(f"||{quote}||")
        await ctx.send(f"-{author}")
    except Exception as e:
        print("Error fetching quote:", e)
        await ctx.send("Couldn't fetch an inspirational quote. Try again later.")
bot.run(TOKEN)
