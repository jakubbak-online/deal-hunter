import telebot
from telebot.apihelper import ApiTelegramException

from handle_config import config

# CREATE BOT INSTANCE
bot = telebot.TeleBot(config["API_KEY"])


def notify(offer_id=None,
           offer_name=None,
           offer_price=None,
           offer_negotiation=None,
           offer_condition=None,
           offer_location=None,
           offer_date=None,
           offer_link=None):
    try:
        bot.send_message(
            chat_id=config["USER_ID"],
            protect_content=True,
            text=f"<b>Nowa oferta!</b>"

                 f"\n\n"
                 f"<u>ID</u>\n"
                 f"     {offer_id:15}"

                 f"\n"
                 f"\n"
                 f"<u>Oferty</u>\n"
                 f"     {offer_name:15}"

                 f"\n"
                 f"\n"
                 f"<u>Cena</u>\n"
                 f"     {offer_price:15}"

                 f"\n"
                 f"\n"
                 f"<u>Neg?</u>\n"
                 f"     {offer_negotiation:15}"

                 f"\n"
                 f"\n"
                 f"<u>Stan</u>\n"
                 f"     {offer_condition:15}"

                 f"\n"
                 f"\n"
                 f"<u>Lokalizacja</u>\n"
                 f"     {offer_location:15}"

                 f"\n"
                 f"\n"
                 f"<u>Data</u>\n"
                 f"     {offer_date:15}"

                 f"\n"
                 f"\n"
                 f"<a href='{offer_link}'>Link do oferty</a>",
            parse_mode="HTML")
    except ApiTelegramException:
        print("Check if you're authorized, or if your API key is correct")
