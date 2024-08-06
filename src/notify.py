import threading
import telebot
from telebot.apihelper import ApiTelegramException

from handle_config import config

# CREATE BOT INSTANCE
bot = telebot.TeleBot(config["API_KEY"])

def _notify(offer):
    try:
        bot.send_message(
            chat_id=config["USER_ID"],
            protect_content=True,
            text=f"<b>Nowa oferta!</b>"
            f"\n\n"
            f"<u>ID</u>\n"
            f"     {offer.id:15}"
            f"\n"
            f"\n"
            f"<u>Oferty</u>\n"
            f"     {offer.name:15}"
            f"\n"
            f"\n"
            f"<u>Cena</u>\n"
            f"     {offer.price:15}"
            f"\n"
            f"\n"
            f"<u>Neg?</u>\n"
            f"     {offer.negotiation:15}"
            f"\n"
            f"\n"
            f"<u>Stan</u>\n"
            f"     {offer.condition:15}"
            f"\n"
            f"\n"
            f"<u>Lokalizacja</u>\n"
            f"     {offer.location:15}"
            f"\n"
            f"\n"
            f"<u>Data</u>\n"
            f"     {offer.date:15}"
            f"\n"
            f"\n"
            f"<a href='{offer.link}'>Link do oferty</a>",
            parse_mode="HTML",
        )
    except ApiTelegramException:
        print("Check if you're authorized, or if your API key is correct")

def notify(offer):
    thread = threading.Thread(target=_notify, args=(offer,))
    thread.start()
