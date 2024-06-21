import time
from data import get_random_sentence


class TypingSpeedLogic:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.current_sentence = get_random_sentence()

    def start_test(self):
        self.start_time = time.time()

    def end_test(self):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        return elapsed_time

    def calculate_speed(self, typed_text):
        if typed_text == self.current_sentence:
            elapsed_time = self.end_test()
            words_per_minute = len(typed_text.split()) / (elapsed_time / 60)
            return words_per_minute
        else:
            return None

    def reset_test(self):
        self.start_time = None
        self.end_time = None
        self.current_sentence = get_random_sentence()
