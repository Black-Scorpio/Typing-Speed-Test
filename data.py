import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "Actions speak louder than words.",
    "A picture is worth a thousand words.",
    "When in Rome, do as the Romans do.",
    "The pen is mightier than the sword.",
    "Practice makes perfect.",
    "You can't judge a book by its cover.",
    "Better late than never.",
    "Birds of a feather flock together.",
    "Cleanliness is next to godliness.",
    "Don't bite the hand that feeds you.",
    "Don't count your chickens before they hatch.",
    "Early to bed and early to rise makes a man healthy, wealthy, and wise.",
    "Every cloud has a silver lining.",
    "Fortune favors the brave.",
    "God helps those who help themselves.",
    "Honesty is the best policy.",
    "If it ain't broke, don't fix it.",
    "Laughter is the best medicine.",
    "Necessity is the mother of invention.",
    "No man is an island.",
    "Rome wasn't built in a day.",
    "The early bird catches the worm.",
    "The grass is always greener on the other side.",
    "Time and tide wait for no man.",
    "When the going gets tough, the tough get going.",
    "You can't make an omelette without breaking eggs."
]

def get_random_sentence():
    return random.choice(sentences)
