# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

import pycord
#from discord.commands import Option

from keep_alive import keep_alive

bot = pycord.Bot(pycord.Intents())

@bot.listen(pycord.Ready)
async def on_ready() -> None:
    print('Bot is ready!')

@bot.command()
async def highfive(ctx: pycord.Context) -> None:
    # send a response to the command
    await ctx.send(':raised_hand: High Five!')

view = pycord.View().url_button('Google it!', 'https://google.com')

@bot.command()
async def google(ctx: pycord.Context) -> None:
    iview = view()
    await ctx.send('Just go to Google!', view=iview)

keep_alive()

token = os.environ.get("TOKEN") or ""
bot.run(token)
