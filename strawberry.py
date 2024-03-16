import discord
from discord.ext import commands
 
DISCORD_CHANNEL_ID = 1217099488959664231
DISCORD_BOT_TOKEN = "MTIxNzA5OTcyNjU4ODIxNTM3Ng.GRVm9L.8hvwcj2kgpoHLhsvHExzvCv1ckuD5bWf3PD2BM"
 
if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True
 
    bot = commands.Bot(command_prefix='!', intents=intents)
 
    @bot.event
    async def on_ready():
        print(f'Bot is ready')
        
        channel = bot.get_channel(DISCORD_CHANNEL_ID)
        if channel is None:
            print('채널이 없어요 😂')
            return
        print('안녕하세요? 😊')
    
    bot.run(DISCORD_BOT_TOKEN)