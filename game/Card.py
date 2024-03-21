cards = {
    "1-clubs": "ace_of_clubs.png",
    "1-spades": "ace_of_diamonds.png",
    "1-diamonds": "ace_of_spades.png",
    "1-heart": "ace_of_hearts.png",
    "2-clubs": "2_of_clubs.png",
    "2-spades": "2_of_spades.png",
    "2-diamonds": "2_of_diamonds.png",
    "2-heart": "2_of_hearts.png",
    "3-clubs": "3_of_clubs.png",
    "3-spades": "3_of_spades.png",
    "3-diamonds": "3_of_diamonds.png",
    "3-heart": "3_of_hearts.png",
    "4-clubs": "4_of_clubs.png",
    "4-spades": "4_of_spades.png",
    "4-diamonds": "4_of_diamonds.png",
    "4-heart": "4_of_hearts.png",
    "5-clubs": "5_of_clubs.png",
    "5-spades": "5_of_spades.png",
    "5-diamonds": "5_of_diamonds.png",
    "5-heart": "5_of_hearts.png",
    "6-clubs": "6_of_clubs.png",
    "6-spades": "6_of_spades.png",
    "6-diamonds": "6_of_diamonds.png",
    "6-heart": "6_of_hearts.png",
    "7-clubs": "7_of_clubs.png",
    "7-spades": "7_of_spades.png",
    "7-diamonds": "7_of_diamonds.png",
    "7-heart": "7_of_hearts.png",
    "8-clubs": "8_of_clubs.png",
    "8-spades": "8_of_spades.png",
    "8-diamonds": "8_of_diamonds.png",
    "8-heart": "8_of_hearts.png",
    "9-clubs": "9_of_clubs.png",
    "9-spades": "9_of_spades.png",
    "9-diamonds": "9_of_diamonds.png",
    "9-heart": "9_of_hearts.png",
    "10-clubs": "10_of_clubs.png",
    "10-spades": "10_of_spades.png",
    "10-diamonds": "10_of_diamonds.png",
    "10-heart": "10_of_hearts.png",
    "11-clubs": "jack_of_clubs.png",
    "11-spades": "jack_of_spades.png",
    "11-diamonds": "jack_of_diamonds.png",
    "11-heart": "jack_of_hearts.png",
    "12-clubs": "queen_of_clubs.png",
    "12-spades": "queen_of_spades.png",
    "12-diamonds": "queen_of_diamonds.png",
    "12-heart": "queen_of_hearts.png",
    "13-clubs": "king_of_clubs.png",
    "13-spades": "king_of_spades.png",
    "13-diamonds": "king_of_diamonds.png",
    "13-heart": "king_of_hearts.png",
}

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.number = self.__value_to_number(value)

    def __value_to_number(self, value):
        match value:
            case 1:
                return "Ace"
            case 11:
                return "Joker"
            case 12:
                return "Queen"
            case 13:
                return "King"
            case _:
                return str(value)

    def convert_json(self):
        return {
            'number': self.number,
            'value': self.value,
            'color': self.color,
            'img': cards[f"{self.value}-{self.color}"]
        }

    def __str__(self):
        return f"{self.number} of {self.color}"