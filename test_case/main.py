import discord
from discord.ext import commands
from dotenv import load_dotenv

import dpyhr

load_dotenv()
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.load_extension("cogs.hello_world")


dpyhr.run(bot, "cogs", selection=dpyhr.Selection.polling)

bot.run(os.getenv("TOKEN"))
