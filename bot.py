from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import os

# Команда /start — кнопка "Начать"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("Начать")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("Нажмите кнопку ниже, чтобы начать:", reply_markup=reply_markup)

# После нажатия "Начать"
async def handle_start_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Добрый день! Я помощник Клуба Городского Жителя — сокращённо КГЖ."
    keyboard = [
        [KeyboardButton("Узнать кто представитель клуба КГЖ")],
        [KeyboardButton("Подписаться на соцсети представителя")],
        [KeyboardButton("Поддержать представителя в голосовании")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(text, reply_markup=reply_markup)

# Обработка всех остальных кнопок
async def handle_menu_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Узнать кто представитель клуба КГЖ":
        await update.message.reply_text("Представитель клуба КГЖ — Иван Иванов, активист района Центральный.")
    elif text == "Подписаться на соцсети представителя":
        await update.message.reply_text("Подписывайтесь на Telegram: https://t.me/kgj_representative")
    elif text == "Поддержать представителя в голосовании":
        await update.message.reply_text("Проголосовать можно по ссылке: https://example.com/vote")
    else:
        await update.message.reply_text("Выберите один из пунктов меню.")

# Подключение токена и регистрация команд
app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^Начать$"), handle_start_button))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_choice))

app.run_polling()
