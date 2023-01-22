import discord
from discord.ext import commands
from dotenv import load_dotenv

import dpyhr

dpyhr.enable_log()

load_dotenv()
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.load_extension("cogs.hello_world")


dpyhr.run("cogs", bot=bot, selection=dpyhr.Selection.polling)

import logging

logging.basicConfig(level=logging.DEBUG)

bot.run(os.getenv("TOKEN"))
