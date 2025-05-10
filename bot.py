
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

okrugs = {
    1: ("Павел Александрович Цуканов", "https://vk.com/pavel.tsukanov48"),
    2: ("Сергей Васильевич Сазонов", "https://vk.com/svsazonov"),
    3: ("Олег Владимирович Косолапов", "https://vk.com/id597083208"),
    4: ("Василий Алексеевич Литовкин", "https://vk.com/id714688672"),
    5: ("Анна Валерьевна Широких", "https://vk.com/id352507585"),
    6: ("Вадим Николаевич Негробов", "https://vk.com/id288778777"),
    7: ("Кирилл Викторович Иванов", "https://vk.com/ivanov_kb"),
    8: ("Юрий Анатольевич Шкарин", "https://vk.com/id565972891"),
    9: ("Михаил Юрьевич Русаков", "https://vk.com/mikhaelrusakov"),
    10: ("Артем Николаевич Голощапов", "https://vk.com/a.goloshchapov"),
    11: ("Андрей Викторович Выжанов", "https://vk.com/avyzhanov"),
    12: ("Евгения Вальерьевна Фрай", "https://vk.com/evgenyafrai"),
    13: ("Сергей Викторович Попов", "https://vk.com/id917351362"),
    14: ("Станислав Алексеевич Полосин", "https://vk.com/stanislavpolosin48"),
    15: ("Екатерина Алексеевна Пинаева", "https://vk.com/pinaeva_ea"),
    16: ("Вера Ивановна Урываева", "https://vk.com/urivaevavi"),
    17: ("Глеб Игоревич Гутевич", "https://vk.com/id1037188881"),
    18: ("Игорь Николаевич Подзоров", "https://vk.com/inpodzorov"),
    19: ("Евгений Сергеевич Колесников", ""),
    20: ("Алексей Иванович Поляков", ""),
    21: ("Павел Викторович Рухлин", "https://vk.com/pavelrukhlin"),
    22: ("Елена Александровна Есина", "https://vk.com/id156008190"),
    23: ("Игорь Александрович Катасонов", "https://vk.com/id1038206450"),
    24: ("Андрей Владимирович Огородников", ""),
    25: ("Галина Николаевна Селина", ""),
    26: ("Алина Евгеньевна Теперик", "https://vk.com/malinateperik"),
    27: ("Владислав Александрович Аленин", "https://vk.com/id1043676620"),
    28: ("Дмитрий Анатольевич Гладышев", "https://vk.com/id152531671"),
    29: ("Дмитрий Николаевич Погорелов", "https://vk.com/id596326492"),
    30: ("Андрей Викторович Иголкин", "https://vk.com/igolkin83"),
    31: ("Андрей Васильевич Бугаков", "https://vk.com/id132130001"),
    32: ("Станислав Геннадьевич Каменецкий", "https://vk.com/id301354842"),
    33: ("Борис Владимирович Понаморев", "https://vk.com/okrug33"),
    34: ("Татьяна Сергеевна Шипилова", "https://vk.com/kaverinats"),
    35: ("Александр Семёнович Перевозчиков", "https://vk.com/id15070507"),
    36: ("Сергей Николаевич Евсеев", "https://vk.com/sergeyevseev48")
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("Начать")]]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("Нажмите кнопку ниже, чтобы начать:", reply_markup=markup)

async def handle_start_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "Добрый день! Я помощник Клуба Городского Жителя — сокращённо КГЖ."
    keyboard = [
        [KeyboardButton("Узнать кто представитель клуба КГЖ")],
        [KeyboardButton("Подписаться на соцсети представителя")],
        [KeyboardButton("Поддержать представителя в голосовании")]
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(msg, reply_markup=markup)

async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Узнать кто представитель клуба КГЖ":
        keyboard = [[KeyboardButton("Не знаю")]]
        markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Напиши номер своего избирательного округа (от 1 до 36):", reply_markup=markup)
    elif text == "Подписаться на соцсети представителя":
        await update.message.reply_text("Подпишись на ВК-страницу: https://vk.com/kgj_club")
    elif text == "Поддержать представителя в голосовании":
        await update.message.reply_text("Голосование доступно по ссылке: https://example.com/vote")

async def handle_district(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.lower() == "не знаю":
        msg = (
            "Как узнать номер округа?:\n\n"
            "- перейди по ссылке: http://www.cikrf.ru/digital-services/nayti-svoy-izbiratelnyy-uchastok/\n"
            "- введи название города, улицу и дом\n"
            "- нажми 'Найти' и получи номер УИК\n"
            "- напиши мне номер УИК в формате 00-00"
        )
        await update.message.reply_text(msg.replace("\n", "\n"))
        return

    try:
        num = int(text)
        if num in okrugs:
            name, link = okrugs[num]
            msg = f"Твой округ: {num}\nПредставитель Клуба Городского Жителя: {name}"
            if link:
                msg += f"\n\nПодпишись на него в социальной сети ВК: {link}"
            keyboard = [[KeyboardButton("Назад")]]
            markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            await update.message.reply_text(msg.replace("\n", "\n"), reply_markup=markup)
        else:
            await update.message.reply_text("Такого округа нет. Введите число от 1 до 36.")
    except ValueError:
        await update.message.reply_text("Пожалуйста, введите номер округа цифрой.")

async def handle_back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "Назад":
        await handle_start_button(update, context)

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^Начать$"), handle_start_button))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^Назад$"), handle_back))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^(Узнать кто|Подписаться|Поддержать)"), handle_main_menu))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_district))
app.run_polling()
