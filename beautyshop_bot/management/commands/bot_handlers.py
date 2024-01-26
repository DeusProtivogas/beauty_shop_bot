from .bot_utils import main_keyboard

from beautyshop_bot.db_utils import get_salon_contacts


def greet_user(update, context):
    chat_id = update.effective_chat.id
    with open('static/greting_salon.jpg', 'rb') as photo_file:
        context.bot.send_photo(chat_id=chat_id, photo=photo_file)

    welcome_message = 'Приветствуем в нашем боте. 🌹🌹🌹 Поможем выбрать услугу, записаться к мастеру в удобное для вас время.'
    update.message.reply_text(welcome_message, reply_markup=main_keyboard())


def show_contacts(update, contex):
    chat_id = update.effective_chat.id

    contacts = get_salon_contacts()

    answer_message = f"У нас есть следующие салоны:\n\n"
    for salon in contacts:
        answer_message += f"Салон: {salon['name']}\n"
        answer_message += f"Адрес: {salon['address']}\n"
        answer_message += f"Телефон: {salon['phone']}\n"
        answer_message += f"\n"

    update.message.reply_text(answer_message, reply_markup=main_keyboard())
