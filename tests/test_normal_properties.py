import unittest

import discord
import discord.ext.commands as commands

import dpyhr


class TestCase(unittest.TestCase):
    def test_raise_on_accessing_forbidden_function(self):
        with self.assertRaises(RuntimeError):
            dpyhr.normal.start()

    def test_utils_is_bot(self):
        self.assertTrue(
            dpyhr.utils.is_bot(
                commands.Bot(command_prefix=".", intents=discord.Intents.all())
            )
        )
        self.assertFalse(dpyhr.utils.is_bot("test"))

    def test_utils_is_coro(self):
        async def test():
            return "i love men"

        self.assertTrue(dpyhr.utils.is_coro(test))
        self.assertFalse(dpyhr.utils.is_coro(lambda: "n word pass"))
        self.assertFalse(dpyhr.utils.is_coro(test()))  # become object

    def test_utils_runner(self):
        def test():
            print("hello")

        async def test2():
            print("hi")

        # check if any error was spitted out
        self.assertIsNone(dpyhr.utils.runner(test))
        self.assertIsNone(dpyhr.utils.runner(test2))
        # now for ultimate test
        try:
            dpyhr.utils.runner(test2())  # suppose to error
        except TypeError:
            pass  # expected since runner expect function not object
        else:
            self.fail("runner() didn't error when it should have")
        try:
            dpyhr.utils.runner(test())  # suppose to error
        except TypeError:
            pass  # expected since runner expect function not object
        else:
            self.fail("runner() didn't error when it should have")

    def test_utils_prevent_calling_outside_dpyhr(self):
        @dpyhr.utils.prevent_calling_outside_dpyhr
        def test():
            return "hello"

        with self.assertRaises(RuntimeError):
            test()


if __name__ == "__main__":
    unittest.main()
