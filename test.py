from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler

# ============================================
# УКАЖИТЕ СЮДА ДАННЫЕ ВАШЕГО БОТА:
# ============================================
BOT_TOKEN = "8534379117:AAHQ6iHykbjedmOXrHs6gJWSpghoznlRqkY"  # Получить от @BotFather в Telegram
WEBAPP_URL = "https://nzaliznyak228.github.io/my-year-review/app.html"  # Замените на URL вашего веб-приложения
# ============================================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Команда /start - показывает кнопку для открытия Mini App"""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Открыть приложение", web_app=WebAppInfo(url=WEBAPP_URL))]
    ])
    await update.message.reply_text(
        "Привет! Нажмите на кнопку чтобы открыть приложение:",
        reply_markup=keyboard
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик любого сообщения - отвечает цифрой 1"""
    await update.message.reply_text("1")


def main() -> None:
    """Запуск бота"""
    # Создаём приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Добавляем обработчик для всех текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    application.run_polling()


if __name__ == "__main__":
    main()
