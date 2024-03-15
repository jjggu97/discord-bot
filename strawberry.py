import discord

TOKEN = 'ADD TOKEN'
CHANNEL_ID = 'ADD CHANNEL ID'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:  
            return

        if message.content.startswith('!strawberry'): 
            await message.channel.send("Hello! 🍓")

intents = discord.Intents.default()
intents.messages = True

client = MyClient(intents=intents)
client.run(TOKEN)
