import discord
from discord.ext import commands
from discord import app_commands

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



TOKEN = open("token.txt", "r").read()
bot.run(TOKEN)