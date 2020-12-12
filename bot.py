
# HELPFUL LINK FOR HEROKU
# https://stackoverflow.com/questions/52247301/how-do-i-host-my-discord-py-bot-on-heroku

import os

import discord
# from dotenv import load_dotenv

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CAP_ID = int(os.getenv('CAP_ID'))
MY_ID = int(os.getenv('MY_ID'))

client = discord.Client()

@client.event
async def on_message(message):

    if message.author.id != CAP_ID:
        return

    capWarning = "***Some or all of the content shared in the above message may be misleading***"
    await message.channel.send(capWarning)

client.run(TOKEN)
