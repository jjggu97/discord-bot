import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message):
    if message.author == client.user: 
        return

    if message.content.startswith('$hello'): 
        await message.channel.send('Hello! 🍓') 

# ADD YOUR TOKEN
client.run('MTIxNzA5OTcyNjU4ODIxNTM3Ng.GlEu2_.Kj9eL-dElgLEn5JrT_2cZBBqfHzhAnJ2jF9ziA') 