import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('The bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server!')

# Commands

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# The star allows you to take multiple arguments and combine it as one. Sort of line String... in java
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
        'Most definitely not',
        'You are dumb',
        'Stop running this command',
        'Yes Senpai',
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
