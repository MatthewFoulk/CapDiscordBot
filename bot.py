
# HELPFUL LINK FOR HEROKU
# https://stackoverflow.com/questions/52247301/how-do-i-host-my-discord-py-bot-on-heroku

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CAP_ID = int(os.getenv('CAP_ID'))
MY_ID = int(os.getenv('MY_ID'))

# Prefix for bot commands
bot = commands.Bot(command_prefix='!')

# Discrimination mode
discriminate = False


# Set the activity of CapBot
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Stop the Cap'))


@bot.command(name='cap', help='Warns about possible lies')
async def cap(ctx):

    # Must be admin to use the bot when slow mode is activated
    if discriminate and not ctx.message.author.guild_permissions.administrator: 
        return
        
    capWarning = "***Some or all of the content shared in the above messages may be misleading***"
    await ctx.send(capWarning)

@bot.command(name='discriminate', help='Requires admin priviledge to use !cap command')
@commands.has_permissions(administrator=True)
async def discriminate(ctx):
    
    global discriminate
    discriminate = True

    message = "*Discrimination mode is now activated*"
    await ctx.send(message)

@bot.command(name='communism', help='Returns !cap command usage to everyone')
@commands.has_permissions(administrator=True)
async def communism(ctx):

    global discriminate
    discriminate = False

    message = "*Commmunism mode is now activated*"
    await ctx.send(message)


bot.run(TOKEN)
