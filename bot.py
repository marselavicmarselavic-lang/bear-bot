import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

bear_skins = {
    "🟢 Обычный Bear": [
        "Bear", "Brown Bear", "White Bear", "Polar Bear", "Black Bear", 
        "Panda Bear", "Gummy Bear", "Winnie", "Noob Bear", "Guest Bear", 
        "Bacon Bear", "Classic Bear", "Apple", "Banana", "Bean Tin", 
        "Bear Mesh", "Blueberry", "Brickbattle"
    ],
    "🔵 Необычный Bear": [
        "Cheeseburger Bear", "Hot Dog Bear", "Pizza Bear", "Ice Cream Bear", 
        "Neon Bear", "Zombie Bear", "Mummy Bear", "Skeleton Bear", 
        "Waddle", "Stinky", "Sam", "Yellow Bear", "Basketballer", "Builder", 
        "Burglar", "Buckethead", "Blue Cheese", "Botanist", "Bowler", 
        "Butterfly", "'06 Zombie"
    ],
    "🟣 Редкий Bear": [
        "Red Bear", "Blue Bear", "Green Bear", "Purple Bear", 
        "Golden Gummy Bear", "Ghost Bear", "Alien Bear", "Robot Bear", 
        "Alpha Bear", "Beta Bear", "1903", "3D Glasses", "70's Slasher", 
        "Blood Moon", "BLUE BUFFALO!!", "Bubblegum", "Axolotls", "Aurora", 
        "Archer", "Ash Walker", "Asteroid"
    ],
    "🟠 Эпический Bear": [
        "Malbear", "Evil Bear", "Shadow Bear", "Void Bear", 
        "Clown Bear", "Cyborg Bear", "Steampunk Bear", "Pharaoh Bear", 
        "Gamma Bear", "Delta Bear", "Amalgabear", "Angelic", "Anglod", 
        "Armageddon", "Bane", "Barbershop Trio", "Beady", "Beeps"
    ],
    "🔴 Легендарный Bear": [
        "Glitch Bear", "Radioactive Bear", "Corrupted Bear", "Frostbite Bear", 
        "Magma Bear", "Slendear", "Sparkle Time Bear", "O.O.B", 
        "Phantom Bear", "Molten Bear", "1st Anniversary", "2nd Anniversary", 
        "3rd Anniversary", "4th Anniversary", "5th Anniversary", "6th Anniversary", 
        "7th Anniversary", "8-Bit/Alpha"
    ],
    "✨ Мифический Bear": [
        "A_B_E", "Inverse Bear", "Hallow Bear", "Chronomancer Bear", 
        "Dark Matter Bear", "Galaxy Bear", "Nebula Bear", "Omega Bear", 
        "A.N.N.O.B.", "A.S.T.R.O.B.", "A.U.R.O.R.O.B.", "B.A.C.H.E.R.O.B.", 
        "B.A.S.K.O.B.", "B.L.U.M.O.B.", "C.A.C.T.O.B.", "C.A.N.V.O.B.", 
        "C.A.R.D.I.O.B.", "C.A.R.D.O.B."
    ],
    "👑 Божественный Bear": [
        "The Overseer", "Ancient Bear", "Lord Bear", "Eternal Void", 
        "Crystal Bear", "Corrupted B.O.B", "Alpha (Bear)", "Alpha (Survivor)", 
        "Area 51 Green Thing", "AREA 51 PASTA CREATURE"
    ],
    "⬛ Секретный Bear": [
        "Afrocity", "Atrocity", "8-B.O.B.", "Alakasam", "Bear/2018 Prototype"
    ]
}

rarity_names = list(bear_skins.keys())
rarity_weights = [35, 25, 17, 10, 7, 4.5, 1.2, 0.3]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Напиши /bear и выбей один из 70+ скинов Bear(Alpha)! 🎰\n\nШанс на Секретный скин всего 0.3%!")

async def bear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rarity = random.choices(rarity_names, weights=rarity_weights, k=1)[0]
    skin = random.choice(bear_skins[rarity])
    if rarity == "⬛ Секретный Bear":
        response = (f"🚨 **НЕВЕРОЯТНАЯ УДАЧА! ШАНС 0.3%!** 🚨\n\n"
                    f"🏅 Редкость: {rarity}\n🐻 Скин: **{skin}**")
    else:
        response = (f"🎰 **Крутим рулетку Bear(Alpha)...**\n\n"
                    f"🏅 Редкость: {rarity}\n🐻 Скин: **{skin}**")
    await update.message.reply_text(response, parse_mode="Markdown")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bear", bear))
    app.run_polling()
