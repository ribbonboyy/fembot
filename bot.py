import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands
from pymongo import MongoClient
from keep_alive import keep_alive

# ===== Load Environment section =====
load_dotenv()
print("MONGO_URI exists:", "✅" if os.getenv("MONGO_URI") else "❌")

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["fembot"]

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

# ===== Images storage =====
femboy_images = [
    "https://images.steamusercontent.com/ugc/1005933590987309852/F0BD73B0E6B73AA12C9228B3F29AA11FB266CC78/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false",
    "https://images.steamusercontent.com/ugc/1656726094523869119/665C09AAA721675E6ECEA78936140BEA0AFF91B3/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false",
    "https://megamousearts.com/wp-content/uploads/2023/09/IMG-8124.jpg",
]

tomboy_images = [
    "https://preview.redd.it/who-are-the-best-anime-tomboys-v0-xl8a3dkw01qe1.png?width=450&auto=webp&s=df24c7eb98c0b337bdc817328cbbc6a0fce2d492",
    "https://photos.yodayo.com/8fefd5ca-9d2d-405d-9e68-e1328e507b9e.png",
    "https://i.pinimg.com/736x/74/78/f3/7478f3e3b99c9174f88e52747990261c.jpg",
]

cat_images = [
    "https://i.guim.co.uk/img/media/327aa3f0c3b8e40ab03b4ae80319064e401c6fbc/377_133_3542_2834/master/3542.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=34d32522f47e4a67286f9894fc81c863",
    "https://www.alleycat.org/wp-content/uploads/2019/03/FELV-cat.jpg",
    "https://cdn.britannica.com/39/226539-050-D21D7721/Portrait-of-a-cat-with-whiskers-visible.jpg",
]

# ===== Bot events =====
@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

@bot.command()
async def tomboy(ctx):
    await ctx.send(random.choice(tomboy_images))

@bot.command()
async def cat(ctx):
    await ctx.send(random.choice(cat_images))

@bot.command()
async def femboy(ctx):
    await ctx.send(random.choice(femboy_images))
    
@bot.command()
async def dice(ctx, sides: int = 6):
    result = random.randint(1, sides)
    embed = discord.Embed(
        title="🎲 Dice Roll",
        description=f"You rolled a **{result}** (1–{sides})",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

@bot.command()
async def eightball(ctx, *, question):
    responses = [
        "Yes.", "No.", "Maybe.", "Definitely!", "Absolutely not.",
        "Ask again later.", "I have no idea.", "Sure!", "Unlikely."
    ]
    embed = discord.Embed(
        title="🎱 Magic 8 Ball",
        description=f"**Question:** {question}\n**Answer:** {random.choice(responses)}",
        color=discord.Color.purple()
    )
    await ctx.send(embed=embed)

# ===== Economy System =====
def get_balance(user_id):
    user = db.users.find_one({"_id": user_id})
    if not user:
        user = {"_id": user_id, "balance": 0}
        db.users.insert_one(user)
    return user["balance"]

def update_balance(user_id, amount):
    db.users.update_one({"_id": user_id}, {"$inc": {"balance": amount}}, upsert=True)

@bot.command()
async def balance(ctx):
    bal = get_balance(ctx.author.id)
    embed = discord.Embed(
        title="💰 Balance",
        description=f"{ctx.author.mention}, you have **{bal} coins**.",
        color=discord.Color.gold()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def work(ctx):
    amount = random.randint(100, 500)
    update_balance(ctx.author.id, amount)
    embed = discord.Embed(
        title="💼 Work",
        description=f"{ctx.author.mention} worked hard and earned **{amount} coins!**",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    amount = random.randint(1, 50)
    update_balance(ctx.author.id, amount)
    embed = discord.Embed(
        title="🪙 Begging",
        description=f"{ctx.author.mention} begged and got **{amount} coins.**",
        color=discord.Color.orange()
    )
    await ctx.send(embed=embed)

@bot.command()
async def coinflip(ctx, amount: int):
    bal = get_balance(ctx.author.id)

    if amount <= 0:
        embed = discord.Embed(description="❌ You must bet more than 0 coins.", color=discord.Color.red())
        return await ctx.send(embed=embed)
    if bal < amount:
        embed = discord.Embed(description="❌ You don’t have enough coins to bet that much.", color=discord.Color.red())
        return await ctx.send(embed=embed)

    result = random.choice(["win", "lose"])
    if result == "win":
        update_balance(ctx.author.id, amount)
        embed = discord.Embed(
            title="🪙 Coin Flip",
            description=f"{ctx.author.mention} flipped **heads** and won **{amount} coins! 🎉**",
            color=discord.Color.green()
        )
    else:
        update_balance(ctx.author.id, -amount)
        embed = discord.Embed(
            title="💀 Coin Flip",
            description=f"{ctx.author.mention} flipped **tails** and lost **{amount} coins.**",
            color=discord.Color.red()
        )
    await ctx.send(embed=embed)

@bot.command()
async def leaderboard(ctx):
    top_users = db.users.find().sort("balance", -1).limit(10)
    embed = discord.Embed(title="🏆 Leaderboard", color=discord.Color.blurple())

    rank = 1
    for user in top_users:
        try:
            member = ctx.guild.get_member(int(user["_id"]))
            name = member.name if member else "Unknown User"
            embed.add_field(
                name=f"#{rank} {name}",
                value=f"💰 {user['balance']} coins",
                inline=False
            )
            rank += 1
        except Exception as e:
            print(f"Error in leaderboard for user {user['_id']}: {e}")

    await ctx.send(embed=embed)

# ===== Run Bot =====
keep_alive()
bot.run(TOKEN)
