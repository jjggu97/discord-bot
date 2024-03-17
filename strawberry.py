import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '안녕':
        await message.channel.send('안녕하세요!')

client.run('여러분의 디스코드 봇 토큰을 입력하세요')
