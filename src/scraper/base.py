import os
import pickle
from enum import Enum

# MY IMPORTS
from notify import notify
from data.pickle_helper import clear_file
from time_utils import measure_time

# VARIABLES FROM CONFIG
from config import ALREADY_NOTIFIED_PATH

class Offer:
    """Represents an offer scraped from OLX."""
    def __init__(self, id: str, name: str, price: str, negotiation: str, condition: str, location: str, date: str, link: str) -> None:
        self.id=id
        self.name=name
        self.price=price
        self.negotiation=negotiation
        self.condition=condition
        self.location=location
        self.date=date
        self.link=link

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Offer):
            return False

        return (
            self.id == other.id and
            self.name == other.name and
            self.price == other.price and
            self.negotiation == other.negotiation and
            self.condition == other.condition and
            self.location == other.location and
            self.date == other.date and
            self.link == other.link
        )

    def __hash__(self) -> int:
        return int(self.id)

    def __str__(self) -> str:
        return (
f"""
{self.name} ({self.id})
    - {self.price}, {self.negotiation}
    - {self.condition}
    - {self.location}
    - {self.date}
    - {self.link}
"""
)

# this must be here to prevent import issues, untill proper module initialization is implemented
from . import search_loader, search_selenium, search_bs

class Backend(Enum):
    SELENIUM = 1
    BEAUTIFUL_SOUP = 2

@measure_time.measure_time
def search_offers(backend: Backend = Backend.SELENIUM) -> None:
    match backend:
        case Backend.SELENIUM:
            offers = search_selenium.search_selenium()
        case Backend.BEAUTIFUL_SOUP:
            offers = search_bs.search_bs()

    # notifications
    if (not os.path.isfile(ALREADY_NOTIFIED_PATH)):
        clear_file()

    with open(ALREADY_NOTIFIED_PATH, "rb") as f:
        already_notified = pickle.load(f)

    for count, offer in enumerate(offers, 1):
        if offer in already_notified:
            continue

        notify(offer)

        match count:
            case 1:
                suffix = "st"
            case 2:
                suffix = "nd"
            case 3:
                suffix = "rd"
            case _:
                suffix = "th"

        print(
            f"\tNotified user about offer {offer.id:9}. "
            f"It was the {count}{suffix} offer"
        )

        with open(ALREADY_NOTIFIED_PATH, "wb") as f:
            already_notified.add(offer)
            pickle.dump(already_notified, f, protocol=pickle.HIGHEST_PROTOCOL)
