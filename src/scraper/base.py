from . import search_loader

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
