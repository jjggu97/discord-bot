import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')

# enter discord bot token
bot.run('YOUR_BOT_TOKEN')

# bot is ready
@bot.event
async def on_ready():
    print('Bot is ready.')

# cmd - ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# cmd - say
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

# cmd - kick
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked.')

# cmd - ban
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned.')
