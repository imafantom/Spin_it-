import tkinter as tk
import random

# Sample data
vocabulary = [
    {"word_en": "apple", "word_pl": "jabłko", "sentence": "I ate an apple for breakfast."},
    {"word_en": "book", "word_pl": "książka", "sentence": "She borrowed a book from the library."},
    {"word_en": "car", "word_pl": "samochód", "sentence": "He drives a red car."},
    {"word_en": "dog", "word_pl": "pies", "sentence": "The dog is barking loudly."},
    {"word_en": "house", "word_pl": "dom", "sentence": "They live in a beautiful house."}
]

# Function to select a random word
def spin_word():
    choice = random.choice(vocabulary)
    word_label.config(text=f"{choice['word_en']} / {choice['word_pl']}")
    sentence_label.config(text=choice['sentence'])

# Create the main application window
root = tk.Tk()
root.title("Spin It! English-Polish Vocabulary Game")

# Word display
word_label = tk.Label(root, text="Spin to get a word!", font=("Helvetica", 16))
word_label.pack(pady=20)

# Sentence display
sentence_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=400)
sentence_label.pack(pady=20)

# Button to spin
spin_button = tk.Button(root, text="Spin it!", font=("Helvetica", 14), command=spin_word)
spin_button.pack(pady=20)

# Run the application
root.mainloop()
