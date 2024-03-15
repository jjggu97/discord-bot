import discord
from datetime import datetime

TOKEN = 'MTIxNzA5OTcyNjU4ODIxNTM3Ng.GR82nQ.9Zc5rbWX-oSv9PLAXNUZ3phVqmL7jU4JH26o8U'
CHANNEL_ID = '1217099488959664231'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(status=discord.Status.online, activity=discord.Game("strawberry"))

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if "오늘" in message.content:
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            await message.channel.send(f"지금은 {current_time} 입니다.")

intents = discord.Intents.default()
intents.messages = True
client = MyClient(intents=intents)
client.run(TOKEN)
