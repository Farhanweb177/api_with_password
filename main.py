from fastapi import FastAPI
import random

app = FastAPI()


side_hustle = [
    "Freelance graphic design",
    "Online tutoring",
    "Affiliate marketing",
    "Sell digital products (eBooks, templates)",
    "Start a dropshipping business",
    "Social media management",
    "Create a YouTube channel",
    "Offer web development services",
    "Pet sitting or dog walking",
    "Become a virtual assistant"
]

money_quotes = [
    "Don’t work for money; make it work for you. – Robert Kiyosaki",
    "The goal isn’t more money. The goal is living life on your terms. – Chris Brogan",
    "It’s not your salary that makes you rich, it’s your spending habits. – Charles A. Jaffe",
    "Money grows on the tree of persistence. – Japanese Proverb",
    "Never depend on a single income. Make investment to create a second source. – Warren Buffett",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "Beware of small expenses; a small leak will sink a great ship. – Benjamin Franklin",
    "The best investment you can make is in yourself. – Warren Buffett"
]


@app.get("/side_hustle")
def get_side_hustle():
    """Return a random side_hustle idea"""
    return {"side_hustle": random.choice(side_hustle)}

@app.get("/money_quotes")
def get_side_hustle():
    """Return a random money_quotes idea"""
    return {"money_quotes": random.choice(money_quotes)}