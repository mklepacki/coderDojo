import discord
from secret import BOT_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('Jestem gotowy do dzialania, nazywam sie {}'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!hello'):
        print(message.content)
        message_contents = message.content.split(' ')

        await message.channel.send('Hello <@{}>, nice to see you! There are {} arguments: {}'.format(message.author.id, len(message_contents), message_contents))

    if message.content == '!github':
        await message.channel.send('https://github.com/mklepacki/coderDojo/')

    if message.content == '!kizo':
        await message.channel.send('https://www.youtube.com/watch?v=XE5G004diWE')
    

client.run(BOT_TOKEN)