import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NzM4NTQ4OTE0NjkyODE2OTU2.XyNhRg.hsaHSbgvik1QBMcz3j3sjvOz2gA')