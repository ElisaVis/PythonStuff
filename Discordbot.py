import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import command

#this is just an extremely simple bot just to show you how to begin to make one

client = commands.Bot(command_prefix="!")
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def yeet(ctx):
    await ctx.send("sauce")

@client.command()
async def ping(ctx):
    await ctx.send("pong")

client.run("YOUR TOKEN") #put in your bot's token here
