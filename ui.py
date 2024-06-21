import tkinter as tk
from logic import TypingSpeedLogic


class TypingSpeedUI:
    def __init__(self, root):
        self.root = root
        self.logic = TypingSpeedLogic()
        self.root.title("Typing Speed Test")
        self.root.geometry("800x400")
        self.root.configure(bg="#f0f0f0")

        self.setup_ui()

    def setup_ui(self):
        self.instruction_label = tk.Label(self.root, text="Type the sentence below and press Enter.",
                                          font=("Helvetica", 14), bg="#f0f0f0")
        self.instruction_label.pack(pady=(20, 10))

        self.label_text = tk.Label(self.root, text=self.logic.current_sentence, font=("Helvetica", 16), bg="#f0f0f0")
        self.label_text.pack(pady=(10, 20))

        self.entry_text = tk.Entry(self.root, font=("Helvetica", 14), width=50, state=tk.DISABLED)
        self.entry_text.pack(pady=(10, 20))
        self.entry_text.bind("<Return>", self.calculate_speed)

        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_countdown,
                                      font=("Helvetica", 14), bg="#4caf50", fg="white")
        self.start_button.grid(row=0, column=0, padx=5)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_test, font=("Helvetica", 14),
                                      bg="#f44336", fg="white")
        self.reset_button.grid(row=0, column=1, padx=5)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16), bg="#f0f0f0")
        self.result_label.pack(pady=(20, 10))

        self.countdown_label = tk.Label(self.root, text="", font=("Helvetica", 16), bg="#f0f0f0")
        self.countdown_label.pack(pady=(20, 10))

    def start_countdown(self):
        self.start_button.config(state=tk.DISABLED)
        self.countdown(5)

    def countdown(self, count):
        self.countdown_label.config(text=f"Begin Typing in .. {count}")
        if count > 0:
            self.root.after(1000, self.countdown, count - 1)
        else:
            self.start_test()

    def start_test(self):
        self.entry_text.config(state=tk.NORMAL)
        self.entry_text.delete(0, tk.END)
        self.entry_text.focus()
        self.logic.start_test()
        self.countdown_label.config(text="")

    def calculate_speed(self, event):
        typed_text = self.entry_text.get()
        speed = self.logic.calculate_speed(typed_text)

        if speed is not None:
            self.result_label.config(text=f"Typing Speed: {speed:.2f} WPM")
        else:
            self.result_label.config(text="Typed text does not match the sample text.")

        self.entry_text.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

    def reset_test(self):
        self.logic.reset_test()
        self.label_text.config(text=self.logic.current_sentence)
        self.entry_text.delete(0, tk.END)
        self.entry_text.config(state=tk.DISABLED)
        self.result_label.config(text="")
        self.countdown_label.config(text="")
        self.start_button.config(state=tk.NORMAL)



