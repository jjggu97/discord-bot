import discord

TOKEN = 'MTIxNzA5OTcyNjU4ODIxNTM3Ng.GR82nQ.9Zc5rbWX-oSv9PLAXNUZ3phVqmL7jU4JH26o8U'
CHANNEL_ID = '1217099488959664231'

class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(int(CHANNEL_ID))
        await channel.send('Strawberry')
 
 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)