from tkinter import *
from tkinter import messagebox
import time


class TypingSpeedTest:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.text = ("The quick brown fox jumps over the lazy dog. "
                     "This sentence contains every letter of the alphabet at least once.")

        self.start_time = None
        self.end_time = None

        self.create_widgets()

    def create_widgets(self):
        self.label = Label(text="Typing Speed Test", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.start_button = Button(text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)

        self.text_display = Text(height=5, wrap='word', padx=10, pady=10)
        self.text_display.pack(pady=10)

        self.text_display.insert(END, self.text)
        self.text_display.config(state='disabled')

        self.input_text = Text(height=5, wrap='word', padx=10, pady=10)
        self.input_text.pack(pady=10)

        self.submit_button = Button(text="Submit", command=self.calculate_speed)
        self.submit_button.pack(pady=10)

    def start_test(self):
        self.input_text.delete("1.0", END)
        self.start_time = time.time()
        self.input_text.focus()

    def calculate_speed(self):
        self.end_time = time.time()
        input_text = self.input_text.get("1.0", END).strip()
        elapsed_time = self.end_time - self.start_time
        word_count = len(input_text.split())
        words_per_minute = (word_count / elapsed_time) * 60

        messagebox.showinfo("Typing Speed Test Result", f"Your typing speed is {words_per_minute:.2f} WPM.")

    def run(self):
        self.window.mainloop()

