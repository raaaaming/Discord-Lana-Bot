# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

from keep_alive import keep_alive

from discord.ext import commands

import pycord.wavelink as wavelink


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=">?")

    async def on_ready(self):
        print("Bot is ready!")


class Music(commands.Cog):
    """Music cog to hold Wavelink related commands and listeners."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        """Connect to our Lavalink nodes."""
        await self.bot.wait_until_ready()

        await wavelink.NodePool.create_node(
            bot=self.bot, host="0.0.0.0", port=2333, password="YOUR_LAVALINK_PASSWORD"
        )

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f"Node: <{node.identifier}> is ready!")

    @commands.command()
    async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
        """Play a song with the given search query.

        If not connected, connect to our voice channel.
        """
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(
                cls=wavelink.Player
            )
        else:
            vc: wavelink.Player = ctx.voice_client

        await vc.play(search)

keep_alive()

bot = Bot()
bot.add_cog(Music(bot))
token = os.environ.get("TOKEN") or ""
bot.run(token)
