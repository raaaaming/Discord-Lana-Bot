# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

import discord
#from discord.commands import Option

from keep_alive import keep_alive

client = discord.Bot()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.slash_command(description="인사하기")
async def hello(ctx):
    await ctx.respond(f"안녕하세요!")

keep_alive()

token = os.environ.get("TOKEN") or ""
client.run(token)
