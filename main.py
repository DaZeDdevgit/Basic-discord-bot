import discord
from discord.ext import commands
from discord import app_commands
import random

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", case_insensitive=False, intents=intents)


@bot.event
async def on_ready():
    activity = discord.Game(name="YOUR BOT STATUS HERE")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("-> I'm ready")
    try:
        await bot.tree.sync()
        print("-> Synced the commands")
    except exception as e:
        print(e)


@bot.tree.command()
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.mention}!")


@bot.tree.command()
async def dice(interaction: discord.Interaction):
    embed = discord.Embed(title=":game_die: Dice", description=f"You rolled the dice and got {random.randint(1,6)}!", color=discord.Color.red()) # You can add Options like RGB and more.
    embed.set_thumbnail(url="https://clipground.com/images/clipartdice-clipart-9.png")
    await interaction.response.send_message(embed=embed)




TOKEN = open("token.txt", "r").read()
bot.run(TOKEN)