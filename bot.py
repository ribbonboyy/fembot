from keep_alive import keep_alive
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

femboy_images = [
    "https://images.steamusercontent.com/ugc/1005933590987309852/F0BD73B0E6B73AA12C9228B3F29AA11FB266CC78/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false",
    "https://images.steamusercontent.com/ugc/1656726094523869119/665C09AAA721675E6ECEA78936140BEA0AFF91B3/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false",
    "https://megamousearts.com/wp-content/uploads/2023/09/IMG-8124.jpg",
    "https://m.media-amazon.com/images/I/71CtyelU49L._AC_SL1000_.jpg",
    "https://img.joomcdn.net/4f0e00c8729bf91826536b4bfb000d6c649510f9_original.jpeg",
    "https://shapes.inc/api/public/avatar/astolfo-i84c",
    "https://pm1.aminoapps.com/6953/654c038410caf42e5cc8c7a9967ab9dbe1600c94r1-369-512v2_00.jpg",
    "https://static.wikia.nocookie.net/aesthetics/images/e/e8/Femboy_castiel_onyx.jpg/revision/latest?cb=20230730190533",
    "https://i.redd.it/4enjtq4ga5sd1.jpeg",
    "https://images.uncyclomedia.co/necyklopedie/cs/thumb/5/5a/Femboy_ve_sv%C3%A9_p%C5%99irozen%C3%A9_srsti.jpeg/640px-Femboy_ve_sv%C3%A9_p%C5%99irozen%C3%A9_srsti.jpeg",
    "https://api.fstik.app/file/CAACAgIAAxUAAWkGsHYY_WuQp19IPozY4AUTbH5mAAKdawACMKhxS5VNgiDouwHhNgQ/sticker.webp",
    "https://static.wikia.nocookie.net/topstrongest/images/6/67/Ferris_Character_Art.png/revision/latest?cb=20170207024549",
    "https://i.pinimg.com/736x/c2/24/0d/c2240d74ef1d1b0505fae3fbfc9928c5.jpg",
    "https://i.redd.it/2ec98og6rsna1.png",
    "https://files.shapes.inc/api/files/avatar_13b581ef-5820-48e4-bbf9-8884e7581ac9.png",
    "https://a.allegroimg.com/original/11d03d/08cea9b94c5487e9eadeb6b3801c/Plakat-A3-Re-Zero-Anime-Manga-Felix-Argyle",
    "https://preview.redd.it/happy-birthday-to-me-v0-cgf32gwrzznf1.jpeg?width=640&crop=smart&auto=webp&s=0e3243114be09b05c51f36f6a51f7feb1bd3955d",
    "https://images7.alphacoders.com/858/858728.jpg",
    "https://pm1.aminoapps.com/6925/7dbcdd9a55759f4446e4df1e475147616f966237r1-600-800v2_00.jpg"
]

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

@bot.command()
async def femboy(ctx):
    image = random.choice(femboy_images)
    await ctx.send(image)

keep_alive()  # ✅ starts the web server thread
bot.run(TOKEN)
