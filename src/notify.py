import os

import telebot
from dotenv import find_dotenv, load_dotenv


# IMPORT ENV VARIABLES
load_dotenv(find_dotenv())
API_KEY = os.getenv("API_KEY")
USER_ID = os.getenv("USER_ID")

# CREATE BOT INSTANCE
bot = telebot.TeleBot(API_KEY)


def notify(offer_id=None,
           offer_name=None,
           offer_price=None,
           offer_negotiation=None,
           offer_condition=None,
           offer_location=None,
           offer_date=None,
           offer_link=None):
    bot.send_message(
        chat_id=USER_ID,
        protect_content=True,
        text=f"Nowa oferta! &#10"
             
             f"ID oferty: "
             f"{offer_id} &#10"
             
             f"Nazwa oferty: "
             f"{offer_name} &#10"
             
             f"Cena oferty: "
             f"{offer_price} &#10"
             
             f"Czy do negocjacji: "
             f"{offer_negotiation} &#10"
             
             f"Stan oferty: "
             f"{offer_condition} &#10"
             
             f"Lokalizacja oferty: "
             f"{offer_location} &#10"
             
             f"Data wystawienia oferty: "
             f"{offer_date} &#10"
             
             f"<a href='{offer_link}'>Link do oferty</a>",
        parse_mode="HTML")
