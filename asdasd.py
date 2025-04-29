import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логгирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Конфигурация
TOKEN = "8048604518:AAF62nBqmcSsCSKdngZNSvY468dbIHWG5qA"
GITHUB_FILE_URL = "https://raw.githubusercontent.com/username/repo/main/file.txt"  # Замените на ваш RAW-URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет файл при команде /start."""
    try:
        await update.message.reply_document(
            document=GITHUB_FILE_URL,
            caption="Вот ваш файл с GitHub!"
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        await update.message.reply_text("⚠️ Не удалось отправить файл.")

def main() -> None:
    """Запуск бота."""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
