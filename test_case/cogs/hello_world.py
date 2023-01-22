from discord.ext import commands


class hello_world(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context) -> None:
        await ctx.send("Hello world!")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(hello_world(bot))
