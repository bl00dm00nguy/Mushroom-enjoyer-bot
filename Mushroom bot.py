import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='I_like_mushrooms', help='Responds with "I like them too!"')
async def i_like_mushrooms(ctx):
    await ctx.send("I like them too!")

@bot.command(name='I_dont_like_mushrooms', help='Responds with "That\'s unfortunate."')
async def i_dont_like_mushrooms(ctx):
    await ctx.send("That's unfortunate. Is there something specific you don't like about them?")

@bot.command(name='I_hate_mushrooms', help='Mutes the user for 60 seconds.')
async def i_hate_mushrooms(ctx):
    await mute_user(ctx.author, ctx.guild)
    await ctx.send(f"{ctx.author.mention} has been muted for 60 seconds for expressing hatred towards mushrooms.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "I hate mushrooms" in message.content:
        await mute_user(message.author, message.guild)
        await message.channel.send(f"{message.author.mention} has been muted for 60 seconds for expressing hatred towards mushrooms.")

    await bot.process_commands(message)

async def mute_user(user, guild):
    # Mute the user
    await user.add_roles(discord.utils.get(guild.roles, name="Muted"))

    # Unmute the user after 60 seconds
    await asyncio.sleep(60)
    await user.remove_roles(discord.utils.get(guild.roles, name="Muted"))

# Token of the bot
bot.run('BOT TOKEN')
