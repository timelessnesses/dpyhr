"""
dphyr
A simple module for support hot reloading of discord.py "cogs" (extensions).
"""
import enum
import logging
import typing

log = logging.getLogger("dpyhr")

try:
    import discord.ext.commands as commands
except ImportError as e:
    log.critical(
        "dpyhr detected that discord.py is not found or you're using wrong version of discord.py without discord.ext.commands. Please install one. For reasons why I am not shipped with discord.py please read this.\nhttps://github.com/timelessnesses/dpyhr/blob/main/README.md#why-you-dont-shipped-discordpy-with-this-package"
    )
    raise ImportError(
        "dpyhr detected that discord.py is not found or you're using wrong version of discord.py without discord.ext.commands. Please install one. For reasons why I am not shipped with discord.py please read this.\nhttps://github.com/timelessnesses/dpyhr/blob/main/README.md#why-you-dont-shipped-discordpy-with-this-package"
    )

from .normal import Normal, normal_start
from .polling import Polling, polling_start
from .utils import is_bot

class Selection(enum.Enum):

    polling = Polling
    normal = Normal


def run(
    *paths: str,
    bot: commands.Bot = None,
    selection: Selection = Selection.normal,
    reloader: typing.Callable = None,
    conditional: typing.Callable = None,
    recursive: bool = False,
    **kwargs,
) -> None:
    """Run dphyr in another thread.

    Args:
        *paths (str): Paths you want to watch for cogs. Supply those as argument
        bot (commands.Bot, Optional): For reloading extensions (if reloader doesn't exists)
        selection (Selection, optional): Observer selection. Defaults to Selection.normal.
        reloader (typing.Callable, optional): Reload module with your own function. Defaults to None.
        conditional (typing.Callable, optional): Conditional when event is triggered. Defaults to None.
        recursive (bool, optional): Recursive reloading. Defaults to False.
        **kwargs: Other arguments for observer.
    Returns:
        None: No returns.
    """
    if (not bot or not is_bot(bot)) and not reloader:
        log.critical("No reloader found and can't fallback to bot.reload_extension")
        raise ValueError("No reloader found")
    if not reloader:
        log.warn("No custom reloader found. Falling back to bot.reload_extension")
        reloader = bot.reload_extension
    if not conditional:
        log.warn(
            "No custom conditional function found. Falling back to lambda function that detects if file changed it .py file"
        )
        conditional = lambda event: event.src_path.endswith(".py")
    if selection == Selection.normal:
        normal_start(
            *paths,
            reloader=reloader,
            condition=conditional,
            recursive=recursive,
            **kwargs,
        )
    elif selection == Selection.polling:
        polling_start(
            *paths,
            reloader=reloader,
            condition=conditional,
            recursive=recursive,
            **kwargs,
        )
    else:
        log.critical("Invalid selection")
        raise ValueError("Invalid selection")
    log.info(f"Started {selection.value} observer in another thread")


log.info("fully initalized")
