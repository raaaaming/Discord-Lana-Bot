# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

from keep_alive import keep_alive

import random

import discord

bot = discord.Bot()
token = "bot_token" # 실제 봇 토큰으로 변경

@bot.slash_command(description="Hello World 출력하기") # 슬래시 커맨드 등록
async def helloworld(ctx): # 슬래시 커맨드 이름
    await ctx.respond("Hello World!") # 인터렉션 응답
    
keep_alive()

token = os.environ.get("TOKEN") or ""
bot.run(token)
