# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

import random

import discord
from discord.commands import Option

bot = discord.Bot()

@bot.slash_command(description="라나와 인사하기")
async def 안녕(ctx):
    await ctx.respond("안녕하세요!")

@bot.slash_command(description="라나의 주사위 굴리기")
async def 주사위(ctx, text: Option(int, "원하시는 숫자를 적어주세요!")):
    num = random.randrange(1, text + 1)
    await ctx.respond(f":game_die: *{num}!*")
            
    

token = os.environ.get("TOKEN") or ""
bot.run(token)
