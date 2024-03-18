import discord
from discord.ext import commands

# Create an instance of Bot
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready
@bot.event
async def on_ready():
    print('Bot is ready.')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Say
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

# Command: Kick
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked.')

# Command: Ban
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned.')

# Run the bot
bot.run('YOUR_BOT_TOKEN')
