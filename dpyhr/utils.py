import asyncio
import inspect
import typing

from discord.ext import commands


def is_coro(func: typing.Callable) -> bool:
    return inspect.iscoroutinefunction(func)


def is_bot(bot: object) -> bool:
    return isinstance(bot, commands.Bot)


def runner(
    property: typing.Union[typing.Callable, typing.Coroutine], *args, **kwargs
) -> typing.Optional[typing.Any]:
    return (
        property() if not is_coro(property) else asyncio.run(property(*args, **kwargs))
    )


def prevent_calling_outside_dpyhr(func: typing.Callable) -> typing.Callable:
    def wrapper(
        *paths: str,
        reloader: typing.Callable,
        condition: typing.Callable,
        recursive: bool,
        **kwargs,
    ):
        # check stack if it's not called by dpyhr.run then raise warning
        if not any("__init__.py" in frame.filename for frame in inspect.stack()):
            raise RuntimeError(
                "This function is not intended to be called outside dpyhr.run. Please use dpyhr.run instead."
            )
        return func(
            *paths,
            reloader=reloader,
            condition=condition,
            recursive=recursive,
            **kwargs,
        )

    return wrapper
