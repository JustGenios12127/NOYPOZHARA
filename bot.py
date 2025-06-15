import telebot
import os
from telebot import types

TOKEN = "7980131577:AAFAblXHAitIMAYunCQpNjWJSNb5H1RUf0E"
bot = telebot.TeleBot(TOKEN)

# ==================== ОСНОВНЫЕ КОМАНДЫ ====================

@bot.message_handler(commands=['start'])
def send_welcome(message):
    company_info = """
🔥 *Добро пожаловать в NETPOZHARA!* 🔥

*Мы обеспечиваем комплексную безопасность предприятий:*
- Пожарная безопасность
- Охрана труда
- Антитеррористическая защита
- Санитарно-эпидемиологическая безопасность
    """
    bot.send_message(message.chat.id, company_info, parse_mode="Markdown")
    show_main_menu(message.chat.id)

# ==================== СИСТЕМА МЕНЮ ====================

def show_main_menu(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("Продукты", callback_data="products"),
        types.InlineKeyboardButton("Документы", callback_data="documents"),
        types.InlineKeyboardButton("Офис", callback_data="office"),
        types.InlineKeyboardButton("Ящик", callback_data="mailbox")
    ]
    markup.add(*buttons)
    bot.send_message(chat_id, "📌 Выберите раздел:", reply_markup=markup)

def show_products_menu(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("ПТМ и БиОТ", callback_data="ptm_biot"),
        types.InlineKeyboardButton("Согласительная комиссия", callback_data="sk"),
        types.InlineKeyboardButton("СЭЗ", callback_data="sez"),
        types.InlineKeyboardButton("Антитеррор (АТЗ)", callback_data="atz"),
        types.InlineKeyboardButton("Назад", callback_data="back_to_main")
    ]
    markup.add(*buttons)
    bot.send_message(chat_id, "🔧 Выберите продукт:", reply_markup=markup)

def show_ptm_biot_menu(chat_id):
    markup = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton("Скрипт продаж", callback_data="ptm_script"),
        types.InlineKeyboardButton("Назад", callback_data="products")
    ]
    markup.add(*buttons)
    bot.send_message(chat_id, "🧯 ПТМ и БиОТ:", reply_markup=markup)

def show_sk_menu(chat_id):
    markup = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton("Скрипт продаж", callback_data="sk_script"),
        types.InlineKeyboardButton("Назад", callback_data="products")
    ]
    markup.add(*buttons)
    bot.send_message(chat_id, "🤝 Согласительная комиссия:", reply_markup=markup)

def show_sez_menu(chat_id):
    markup = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton("Скрипт продаж", callback_data="sez_script"),
        types.InlineKeyboardButton("Назад", callback_data="products")
    ]
    markup.add(*buttons)
    bot.send_message(chat_id, "🧼 Санитарно-эпидемиологическая защита:", reply_markup=markup)

def show_atz_menu(chat_id):
    markup = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton("Скрипт продаж", callback_data="atz_script"),
        types.InlineKeyboardButton("Назад", callback_data="products")
    ]
    markup.add(*buttons)
    bot.send_message(chat_id, "🛡 Антитеррористическая защищённость:", reply_markup=markup)

# ==================== СКРИПТЫ ПРОДАЖ ====================

def send_ptm_script(chat_id):
    script = """
🧯 *СКРИПТ ПРОДАЖ ПТМ и БиОТ*

1. *Приветствие:*
Добрый день! Меня зовут [Имя], я из учебного центра NETPOZHARA. По поводу обязательного обучения по пожарной безопасности и охране труда.

2. *Определение потребности:*
У вас есть действующие:
- Удостоверения ПТМ?
- Сертификаты БиОТ?
(Если нет → переходим к пункту 3)

3. *Юридическое обоснование:*
По закону (МВД РК №777/1019):
- Обучение обязательно 1 раз в 3 года
- Требуется для всех сотрудников
- Проверяется при аудитах

4. *Риски:*
Штрафы до 200 МРП + приостановка деятельности

5. *Наше предложение:*
- Онлайн-обучение за 1 день
- Официальные документы
- Поддержка 24/7

6. *Закрытие:*
Когда вам удобно начать обучение?
    """
    bot.send_message(chat_id, script, parse_mode="Markdown")

def send_sk_script(chat_id):
    script = """
🤝 *СКРИПТ ПРОДАЖ СОГЛАСИТЕЛЬНОЙ КОМИССИИ*

1. *Приветствие:*
Здравствуйте! Я [Имя] из NETPOZHARA. По вопросу обязательного обучения членов согласительной комиссии.

2. *Определение потребности:*
В вашей организации 15+ сотрудников? (Если да → требуется комиссия)

3. *Юридическое обоснование:*
Ст. 159 ТК РК требует:
- Создание комиссии
- Обучение членов
- Ведение документации

4. *Риски:*
Штрафы до 160 МРП за отсутствие

5. *Наше предложение:*
- Единственный центр с лицензией Минюста
- Обучение за 1 день
- Полный пакет документов

6. *Закрытие:*
Сколько человек нужно обучить?
    """
    bot.send_message(chat_id, script, parse_mode="Markdown")

def send_sez_script(chat_id):
    script = """
🧼 *СКРИПТ ПРОДАЖ СЭЗ*

1. *Приветствие:*
Добрый день! Я [Имя] из NETPOZHARA. По вопросу санитарно-гигиенического обучения.

2. *Определение потребности:*
Ваши сотрудники работают с:
- Пищевыми продуктами?
- Клиентами?
(Если да → требуется обучение)

3. *Юридическое обоснование:*
Санитарные правила РК требуют:
- Ежегодное обучение
- Наличие сертификатов
- Отметки в сан.книжках

4. *Риски:*
Штрафы до 2000 МРП + конфискация продукции

5. *Наше предложение:*
- Дистанционное обучение
- Официальные документы
- Поддержка на каз/рус языках

6. *Закрытие:*
Сколько человек нужно обучить?
    """
    bot.send_message(chat_id, script, parse_mode="Markdown")

def send_atz_script(chat_id):
    script = """
🛡 *СКРИПТ ПРОДАЖ АНТИТЕРРОРИСТИЧЕСКОЙ ЗАЩИТЫ*

1. *Приветствие:*
Здравствуйте! Я [Имя] из NETPOZHARA. По вопросу антитеррористической защищённости вашего объекта.

2. *Определение потребности:*
У вас бывает более 50 посетителей в день? (ТРЦ, кафе, школа и т.д.)

3. *Юридическое обоснование:*
Закон РК "О противодействии терроризму" требует:
- Паспорт безопасности
- Категорирование объекта
- Обученный персонал

4. *Риски:*
Штрафы + приостановка деятельности

5. *Наше предложение:*
- Полный пакет документов "под ключ"
- Обучение персонала
- Помощь при проверках

6. *Закрытие:*
Где расположен ваш объект?
    """
    bot.send_message(chat_id, script, parse_mode="Markdown")

# ==================== ОБРАБОТКА CALLBACK ====================

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    
    if call.data == "products":
        show_products_menu(chat_id)
    elif call.data == "ptm_biot":
        show_ptm_biot_menu(chat_id)
    elif call.data == "sk":
        show_sk_menu(chat_id)
    elif call.data == "sez":
        show_sez_menu(chat_id)
    elif call.data == "atz":
        show_atz_menu(chat_id)
    elif call.data == "ptm_script":
        send_ptm_script(chat_id)
    elif call.data == "sk_script":
        send_sk_script(chat_id)
    elif call.data == "sez_script":
        send_sez_script(chat_id)
    elif call.data == "atz_script":
        send_atz_script(chat_id)
    elif call.data == "back_to_main":
        show_main_menu(chat_id)
    elif call.data in ["documents", "office", "mailbox"]:
        bot.send_message(chat_id, f"🛠 Раздел '{call.data.capitalize()}' в разработке.")

# ==================== ЗАПУСК ====================

if __name__ == "__main__":
    print("🚀 Бот NETPOZHARA запущен!")
    bot.polling(none_stop=True)