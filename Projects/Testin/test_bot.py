import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is Ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

@client.command()
async def namaskaram(dm):
    await dm.send("Swadika")
client.run('Nzk0NTQ1NDYwMzc4NzMwNDk3.X-8YHw.Q3vNg_XzgAD91rc57xTIqCheQn0')

