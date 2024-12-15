import streamlit as st
import random

# Sample data
vocabulary = [
    {"word_en": "apple", "word_pl": "jabłko", "sentence": "I ate an apple for breakfast."},
    {"word_en": "book", "word_pl": "książka", "sentence": "She borrowed a book from the library."},
    {"word_en": "car", "word_pl": "samochód", "sentence": "He drives a red car."},
    {"word_en": "dog", "word_pl": "pies", "sentence": "The dog is barking loudly."},
    {"word_en": "house", "word_pl": "dom", "sentence": "They live in a beautiful house."}
]

# Title of the app
st.title("Spin It! English-Polish Vocabulary Game")

# Instruction text
st.write("Click the button to get a random English-Polish word pair and a sentence.")

# Button to spin
if st.button("Spin it!"):
    choice = random.choice(vocabulary)
    st.subheader(f"{choice['word_en']} / {choice['word_pl']}")
    st.write(choice["sentence"])
