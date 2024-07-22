from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext
import logging

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Список ссылок для команды /command1
groups = [
    {"name": "Facebook Share 1", "link": "https://www.facebook.com/share/UFHESAqEKyjLLCPK/?mibextid=A7sQZp"},
    {"name": "WhatsApp Group 1", "link": "https://chat.whatsapp.com/2VaMeQdiW3sFrpROAmQOCi"},
    {"name": "WhatsApp Group 2", "link": "https://chat.whatsapp.com/HCk0bJak1w0CktY2IrXUEP"},
    {"name": "WhatsApp Group 3", "link": "https://chat.whatsapp.com/E7f23s3xnfvDCoDdvRqRPg"},
    {"name": "WhatsApp Group 4", "link": "https://chat.whatsapp.com/LOovERW2VJW88kLH8fxqSb"},
    {"name": "WhatsApp Group 5", "link": "https://chat.whatsapp.com/FTxrG7niNL81Riv9rAKqPl"},
    {"name": "WhatsApp Group 6", "link": "https://chat.whatsapp.com/I1Jiki4S0FK0waoZdkm51z"},
    {"name": "WhatsApp Group 7", "link": "https://chat.whatsapp.com/ES6Uo1OE9IV9TFQadLSvYU"},
    {"name": "WhatsApp Group 8", "link": "https://chat.whatsapp.com/KfQ3thxGHkL67CnnCEUSPd"},
    {"name": "WhatsApp Group 9", "link": "https://chat.whatsapp.com/CUtm7InI3BJHxbDoE4els5"},
    {"name": "WhatsApp Group 10", "link": "https://chat.whatsapp.com/FTxrG7niNL81Riv9rAKqPl"},
    {"name": "WhatsApp Group 11", "link": "https://chat.whatsapp.com/CkeE1yKZZNGIEpxxhECuZp"},
    {"name": "Facebook Share 2", "link": "https://www.facebook.com/share/eZHR5iN5yVExc3Ey/?mibextid=A7sQZp"},
]

async def start(update: Update, context: CallbackContext) -> None:
    logging.info("Команда /start получена")
    await update.message.reply_text('Привет! Я ваш бот.')

async def command1(update: Update, context: CallbackContext) -> None:
    logging.info("Команда /command1 получена")
    
    # Формируем список кнопок в два столбца
    keyboard = []
    row = []
    for group in groups:
        row.append(InlineKeyboardButton(group["name"], url=group["link"]))
        if len(row) == 2:  # Максимум 2 кнопки в строке
            keyboard.append(row)
            row = []
    
    if row:  # Добавляем последнюю строку, если она не пустая
        keyboard.append(row)
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Список групп:', reply_markup=reply_markup)

def main() -> None:
    token = '6991825621:AAHfbFFcxfVinsffhxsuDlJL3ZQ7K_0Q9bU'  # Замените на ваш реальный API-токен
    
    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("command1", command1))
    
    logging.info("Бот запущен и прослушивает команды...")
    application.run_polling()

if __name__ == '__main__':
    main()