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

tomboy_images = [
    "https://preview.redd.it/who-are-the-best-anime-tomboys-v0-xl8a3dkw01qe1.png?width=450&auto=webp&s=df24c7eb98c0b337bdc817328cbbc6a0fce2d492"
    "https://photos.yodayo.com/8fefd5ca-9d2d-405d-9e68-e1328e507b9e.png"
    "https://scontent-prg1-1.xx.fbcdn.net/v/t39.30808-6/480212293_624547870520123_5589541149600627377_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=127cfc&_nc_ohc=E0eNlYhPHk8Q7kNvwFRIIm5&_nc_oc=Adnj8KfHhTEFNJHc7sQTLG4DriyM_xU4sihzrULMRNgdY0D7ar76Ky06K_u3ppNrD4w&_nc_zt=23&_nc_ht=scontent-prg1-1.xx&_nc_gid=OmsiMnZvOdnO65YCzn1Ciw&oh=00_AfgsGArTBZy_ypkZ7rX9fm2YN7WoBN9aKfLa7Tsm5Q55FA&oe=69115F3C"
    "https://i.pinimg.com/736x/74/78/f3/7478f3e3b99c9174f88e52747990261c.jpg"
    "https://i.pinimg.com/736x/08/f9/14/08f914e7cd41fc5da8b97178206851d0.jpg"
    "https://preview.redd.it/for-tomboy-tuesday-what-anime-or-manga-do-you-consider-has-v0-d24ojjlfzqmd1.png?width=1080&crop=smart&auto=webp&s=24cc166e830c54373b52beefefafc5ab53591cfd"
    "https://images.squarespace-cdn.com/content/v1/64c41baeb741dd48db90aef0/1701725073241-WV6CM08N6HUH2C9NAFY8/tomo.png"
]

cat_images = [
    "https://placekitten.com/400/400"
]

@bot.command()
async def tomboy(ctx):
    if not tomboy_images:
        await ctx.send("No tomboy images added yet 👀")
        return
    image = random.choice(tomboy_images)
    await ctx.send(image)

@bot.command()
async def cat(ctx):
    if not cat_images:
        await ctx.send("No cat images added yet 🐾")
        return
    image = random.choice(cat_images)
    await ctx.send(image)

