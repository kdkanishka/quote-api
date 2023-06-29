import unittest
from api.quote_generator import QuoteGenerator

class TestQuoteGenerator(unittest.TestCase):
    def test_generate_quote(self):
        quotes = ["quote 1", "quote 2", "quote 3"]
        generator = QuoteGenerator(quotes)

        quote = generator.generate_quote()

        self.assertIn(quote, quotes)

if __name__ == '__main__':
    unittest.main()
