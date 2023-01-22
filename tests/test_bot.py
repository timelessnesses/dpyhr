import subprocess
import unittest
import os

os.chdir("../test_case")

bot_process = subprocess.Popen(["python", "main.py"]) # should grab the .env immediately

normal_helloworld = """
from discord.ext import commands

class hello_world(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context) -> None:
        await ctx.send("Hello world!")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(hello_world(bot))
"""

changed_helloworld = """
from discord.ext import commands

class hello_world(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context) -> None:
        await ctx.send("Hello world!")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(hello_world(bot)); # this should trigger the hot reload
"""

with open("cogs/hello_world.py", "w") as f:
    f.write(normal_helloworld)
    
import time
time.sleep(5) # wait for the bot to load the cog

# now read the console of the bot process

print(bot_process.stdout.read().decode("utf-8").split("\n")[-1])

assert "dpyhr.polling" in bot_process.stdout.read().decode("utf-8").split("\n")[-1] or "dpyhr.normal" in bot_process.stdout.read().decode("utf-8").split("\n")[-1]