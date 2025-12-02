from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)

# ============================================
# УКАЖИТЕ СЮДА ДАННЫЕ ВАШЕГО БОТА:
# ============================================
BOT_TOKEN = "8534379117:AAHQ6iHykbjedmOXrHs6gJWSpghoznlRqkY"  # Получить от @BotFather в Telegram
WEBAPP_URL = "https://nzaliznyak228.github.io/MyYearReview/index.html"  # Замените на URL вашего веб-приложения
# ============================================

START_TEXT = (
    "✨ Узнай, каким был твой 2025 год в Telegram!\n\n"
    "Посмотри, кто анонимно смотрел твои истории, какие слова ты писал чаще всего и многое другое!\n\n"
    "Если не работает приложение, используйте VPN"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет приветственное сообщение с тремя кнопками"""
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Открыть приложение", web_app=WebAppInfo(url=WEBAPP_URL)),
            InlineKeyboardButton("Заглушка 1", callback_data="placeholder_1"),
            InlineKeyboardButton("Заглушка 2", callback_data="placeholder_2"),
        ]
    ])

    # Отправляем сообщение с кнопками
    if update.message:
        await update.message.reply_text(START_TEXT, reply_markup=keyboard)
    elif update.effective_chat:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=START_TEXT, reply_markup=keyboard)


async def placeholder_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает нажатия на заглушки"""
    query = update.callback_query
    if not query:
        return
    # Отвечаем на CallbackQuery (короткое уведомление)
    await query.answer(text="Это заглушка — пока ничего здесь нет.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отвечает на любое текстовое сообщение цифрой 1"""
    if update.message:
        await update.message.reply_text("1")


def main() -> None:
    """Запуск бота"""
    application = Application.builder().token(BOT_TOKEN).build()

    # Хендлеры
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(placeholder_callback, pattern="^placeholder_"))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем поллинг
    application.run_polling()


if __name__ == "__main__":
    main()
