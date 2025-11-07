import os
print("MONGO_URI exists:", "✅" if os.getenv("MONGO_URI") else "❌")

from keep_alive import keep_alive
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random
from pymongo import MongoClient
import os

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["fembot"]

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

tomboy_images = [
    "https://preview.redd.it/who-are-the-best-anime-tomboys-v0-xl8a3dkw01qe1.png?width=450&auto=webp&s=df24c7eb98c0b337bdc817328cbbc6a0fce2d492",
    "https://photos.yodayo.com/8fefd5ca-9d2d-405d-9e68-e1328e507b9e.png",
    "https://i.pinimg.com/736x/74/78/f3/7478f3e3b99c9174f88e52747990261c.jpg",
    "https://i.pinimg.com/736x/08/f9/14/08f914e7cd41fc5da8b97178206851d0.jpg",
    "https://preview.redd.it/for-tomboy-tuesday-what-anime-or-manga-do-you-consider-has-v0-d24ojjlfzqmd1.png?width=1080&crop=smart&auto=webp&s=24cc166e830c54373b52beefefafc5ab53591cfd",
    "https://images.squarespace-cdn.com/content/v1/64c41baeb741dd48db90aef0/1701725073241-WV6CM08N6HUH2C9NAFY8/tomo.png",
    "https://pbs.twimg.com/media/CbpDmZ2UAAAk2ry.jpg",
    "https://d2bzx2vuetkzse.cloudfront.net/fit-in/0x450/unshoppable_producs/c3f28001-a69b-43e7-a2f5-6eeab24b9b21.jpeg",
]

cat_images = [
    "https://i.guim.co.uk/img/media/327aa3f0c3b8e40ab03b4ae80319064e401c6fbc/377_133_3542_2834/master/3542.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=34d32522f47e4a67286f9894fc81c863",
    "https://www.alleycat.org/wp-content/uploads/2019/03/FELV-cat.jpg",
    "https://cdn.britannica.com/39/226539-050-D21D7721/Portrait-of-a-cat-with-whiskers-visible.jpg",
    "https://cdn.mos.cms.futurecdn.net/KHQb3Ny62YxXnCEon4mm43-1920-80.jpg",
    "https://d2zp5xs5cp8zlg.cloudfront.net/image-79322-800.jpg",
    "https://www.shutterstock.com/image-vector/anime-cartoon-character-orange-color-600nw-2407945115.jpg",
    "https://t4.ftcdn.net/jpg/14/62/82/15/360_F_1462821545_cZ2VApsWn2u9xvSr5UwRgDtbGOQUrJXs.jpg",
    "https://res.cloudinary.com/jerrick/image/upload/d_642250b563292b35f27461a7.png,f_jpg,fl_progressive,q_auto,w_1024/w9bpqfuxrvm99gujxuvi.jpg",
    "https://t3.ftcdn.net/jpg/06/31/24/68/360_F_631246817_I2rGhvcVeeoJbAbbiH8UotlgIA64xRcL.jpg",
    "https://otakuusamagazine.com/wp-content/uploads/2023/10/ousa_cat_hero.png",
    "https://media.hswstatic.com/eyJidWNrZXQiOiJjb250ZW50Lmhzd3N0YXRpYy5jb20iLCJrZXkiOiJnaWZcL2dldHR5aW1hZ2VzLTE0MjIzNDI0MDYuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjo4Mjh9fX0=",
    "https://d2zp5xs5cp8zlg.cloudfront.net/image-88409-800.jpg",
    "https://www.scottishspca.org/wp-content/uploads/2024/09/CATS-INVERNESS-JUNE-24-13-1369x913.jpg",
    "https://peninsulavet.com.au/wp-content/uploads/2020/10/CAT-CHAT-3.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3Lgj4bNP5AiIaqQv4-cVHkPLKVHDGeNRnEw&s",
]

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

@bot.command()
async def tomboy(ctx):
    image = random.choice(tomboy_images)
    await ctx.send(image)

@bot.command()
async def cat(ctx):
    image = random.choice(cat_images)
    await ctx.send(image)

@bot.command()
async def femboy(ctx):
    image = random.choice(femboy_images)
    await ctx.send(image)

@bot.command()
async def dice(ctx, sides: int = 6):
    await ctx.send(f"🎲 You rolled a {random.randint(1, sides)} (1-{sides})")

@bot.command()
async def eightball(ctx, *, question):
    responses = [
        "Yes.", "No.", "Maybe.", "Definitely!", "Absolutely not.", 
        "Ask again later.", "I have no idea.", "Sure!", "Unlikely."
    ]
    await ctx.send(f"🎱 Question: {question}\nAnswer: {random.choice(responses)}")

@bot.command()
async def testdb(ctx):
    db.test.insert_one({"user": str(ctx.author), "test": "ok"})
    await ctx.send("✅ Database connection works!")


keep_alive()  # started web server thread
bot.run(TOKEN)
