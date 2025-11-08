import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands
from pymongo import MongoClient
from keep_alive import keep_alive

# ===== Load Environment =====
load_dotenv()
print("MONGO_URI exists:", "✅" if os.getenv("MONGO_URI") else "❌")

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["fembot"]

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

# ===== Images =====
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

# ===== Bot Events =====
@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

# ===== Image Commands =====
@bot.command()
async def tomboy(ctx):
    await ctx.send(random.choice(tomboy_images))

@bot.command()
async def cat(ctx):
    await ctx.send(random.choice(cat_images))

@bot.command()
async def femboy(ctx):
    await ctx.send(random.choice(femboy_images))

# ===== Fun Commands =====
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

# ===== Economy System =====

# Helper: Get or create a user's balance
def get_balance(user_id):
    user = db.users.find_one({"_id": user_id})
    if not user:
        user = {"_id": user_id, "balance": 0}
        db.users.insert_one(user)
    return user["balance"]

# Helper: Update balance by amount (+ or -)
def update_balance(user_id, amount):
    db.users.update_one({"_id": user_id}, {"$inc": {"balance": amount}}, upsert=True)

@bot.command()
async def balance(ctx):
    """Check your balance."""
    bal = get_balance(ctx.author.id)
    await ctx.send(f"{ctx.author.mention}, you have 💰 {bal} coins.")

@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def work(ctx):
    """Earn money by working."""
    amount = random.randint(100, 500)
    update_balance(ctx.author.id, amount)
    await ctx.send(f"💼 {ctx.author.mention} worked hard and earned {amount} coins!")

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    """Beg for a small amount of money."""
    amount = random.randint(1, 50)
    update_balance(ctx.author.id, amount)
    await ctx.send(f"🪙 {ctx.author.mention} begged and got {amount} coins.")

@bot.command()
async def coinflip(ctx, amount: int):
    """Flip a coin to double or lose your bet."""
    bal = get_balance(ctx.author.id)

    if amount <= 0:
        return await ctx.send("❌ You must bet more than 0 coins.")
    if bal < amount:
        return await ctx.send("❌ You don’t have enough coins to bet that much.")

    result = random.choice(["win", "lose"])
    if result == "win":
        update_balance(ctx.author.id, amount)
        await ctx.send(f"🪙 {ctx.author.mention} flipped heads and won {amount} coins! 🎉")
    else:
        update_balance(ctx.author.id, -amount)
        await ctx.send(f"💀 {ctx.author.mention} flipped tails and lost {amount} coins.")

@bot.command()
async def leaderboard(ctx):
    """Show the richest users."""
    top_users = db.users.find().sort("balance", -1).limit(10)
    leaderboard_text = "**🏆 Leaderboard 🏆**\n\n"
    rank = 1
    for user in top_users:
        member = ctx.guild.get_member(user["_id"])
        name = member.name if member else "Unknown User"
        leaderboard_text += f"{rank}. {name} — 💰 {user['balance']} coins\n"
        rank += 1

    await ctx.send(leaderboard_text or "No data yet!")

# ===== Run Bot =====
keep_alive()
bot.run(TOKEN)

