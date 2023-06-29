import random

class QuoteGenerator:
    def __init__(self, quotes):
        self.quotes = quotes

    def generate_quote(self):
        return random.choice(self.quotes)