from flask import Blueprint, jsonify
from .quote_generator import QuoteGenerator

api_bp = Blueprint('api', __name__)

@api_bp.route('/quote', methods=['GET'])
def get_quote():
    quote = QuoteGenerator(QUOTES).generate_quote()
    return jsonify({'quote': quote})

QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"
]