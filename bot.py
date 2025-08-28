from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "ВАШ_ТОКЕН_ОТ_BOTFATHER"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я могу помочь считать калории. Напиши /calories 500")

async def calories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        cal = int(context.args[0])
        await update.message.reply_text(f"Ты ввёл {cal} калорий.")
    except:
        await update.message.reply_text("Напиши: /calories число калорий")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("calories", calories))

app.run_polling()
