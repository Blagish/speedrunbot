import discord
from config import token
from random import choice


def find_speedrun(s):
    for i in search:
        a = s.find(i)
        if a != -1:
            return True
    return False


react = ['dudududu', 'du du du du', 'Du du du du', 'Dudududu',
         'DUDUDUDU', 'DU DU DU DU']
search = ['speedrun', 'speed run', 'spedrun', 'sped run']


client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return None
    text = message.content
    if find_speedrun(text):
        await message.channel.send(choice(react))

client.run(token)
