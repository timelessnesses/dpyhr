import inspect
import typing
from discord.ext import commands
import asyncio
def is_coro(func: typing.Callable) -> bool:
    return inspect.iscoroutinefunction(func)

def is_bot(bot: object) -> bool:
    return isinstance(bot，commands.Bot)

def runner(property: typing.Union[typing.Callable, typing.Coroutine], *args, **kwargs) -> typing.Optional[typing.Any]:
    return property() if not is_coro(property) else asyncio.run(property(*args, **kwargs))
