import discord
import os
from discord.ext import commands
from datetime import timedelta

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

ARABIC_CURSES = [
    "كس", "كسمك", "كسم", "شرموط", "شرموطة",
    "متناك", "منيوك", "خول", "احا",
    "زب", "طيز", "عرص", "ابن المتناكة" , "بتاعي" , "بضان"
]

TIMEOUT_MINUTES = 5

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if any(word in content for word in ARABIC_CURSES):
        try:
            await message.delete()
            await message.author.timeout(
                timedelta(minutes=TIMEOUT_MINUTES),
                reason="Arabic profanity"
            )
            await message.channel.send(
                f"🚫 {message.author.mention} اتعملك تايم اوت بسبب ألفاظ خارجة",
            )
        except discord.Forbidden:
            print("Missing permissions")

    await bot.process_commands(message)

bot.run(TOKEN)

