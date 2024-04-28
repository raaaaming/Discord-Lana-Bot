# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.tree.command(name='hello', description='testing')  # 명령어 이름, 설명
@app_commands.describe(text1='쓸 내용', text2 = '번호') # 같이 쓸 내용들
async def hello(interaction: discord.Interaction, text1:str, text2:int):    # 출력
    await interaction.response.send_message(f'{interaction.user.mention} : {text1} : {text2}', ephemeral=True)

token = os.environ.get("TOKEN") or ""
client.run(token)
