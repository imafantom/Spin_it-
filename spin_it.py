import streamlit as st
import random

# Vocabulary list with sentences
vocabulary = [
    {"word_en": "argue", "word_pl": "kłócić się", "sentence": "They often argue about politics."},
    {"word_en": "siblings", "word_pl": "rodzeństwo", "sentence": "She has two siblings, a brother and a sister."},
    {"word_en": "accusation", "word_pl": "oskarżenie", "sentence": "He denied the accusation against him."},
    {"word_en": "celebrate", "word_pl": "świętować", "sentence": "We will celebrate her birthday tomorrow."},
    {"word_en": "anniversary", "word_pl": "rocznica", "sentence": "Their 10th wedding anniversary is coming up."},
    {"word_en": "gain", "word_pl": "zyskać", "sentence": "She gained a lot of knowledge from the course."},
    {"word_en": "hacker", "word_pl": "haker", "sentence": "The hacker breached the system's security."},
    {"word_en": "independence", "word_pl": "niepodległość", "sentence": "The country celebrates its independence day in July."},
    {"word_en": "short-sighted", "word_pl": "krótkowzroczny", "sentence": "He is very short-sighted when it comes to investments."},
    {"word_en": "look forward to", "word_pl": "nie móc się doczekać", "sentence": "I look forward to meeting you next week."},
    # Add more words here as needed
]

# English grammar trivia
trivia_list = [
    "Did you know? English has no future tense like in many other languages. We use auxiliary verbs to express the future.",
    "In English, 'a' and 'an' are called indefinite articles, and they are used based on whether the following word begins with a vowel sound.",
    "English is a stress-timed language, meaning the rhythm is determined by stressed syllables, not the number of syllables.",
    "The longest English word is 'pneumonoultramicroscopicsilicovolcanoconiosis'!",
    "Some English words, like 'set', have dozens of different meanings depending on context.",
]

# Player stats
if "player_name" not in st.session_state:
    st.session_state["player_name"] = None
if "progress" not in st.session_state:
    st.session_state["progress"] = 0
if "badge" not in st.session_state:
    st.session_state["badge"] = None

# Main game logic
if st.session_state["player_name"] is None:
    st.title("Spin It! Vocabulary Game")
    st.subheader("Enter your name to start the game:")
    name = st.text_input("Your Name")
    if st.button("Let’s have some fun!") and name:
        st.session_state["player_name"] = name
        st.session_state["progress"] = 0
        st.session_state["badge"] = None
else:
    st.title(f"Welcome, {st.session_state['player_name']}! Spin It!")
    st.subheader(f"Your Progress: {st.session_state['progress']} words mastered")
    
    # Display badges based on progress
    badges = [
        {"threshold": 10, "label": "🏅 Rookie"},
        {"threshold": 30, "label": "🥈 Amateur"},
        {"threshold": 40, "label": "🥉 Semi-Pro"},
        {"threshold": 80, "label": "🥇 Pro"},
        {"threshold": 100, "label": "💻 Hacker"},
        {"threshold": 150, "label": "🏆 Legend"},
    ]
    for badge in badges:
        if st.session_state["progress"] >= badge["threshold"]:
            st.session_state["badge"] = badge["label"]
    if st.session_state["badge"]:
        st.write(f"Badge Earned: {st.session_state['badge']}")

    # Button to spin the word
    if st.button("Spin it!"):
        choice = random.choice(vocabulary)
        st.session_state["progress"] += 1
        st.subheader(f"{choice['word_en']} / {choice['word_pl']}")
        st.write(choice["sentence"])

        # Display trivia every 7 words
        if st.session_state["progress"] % 7 == 0:
            trivia = random.choice(trivia_list)
            st.markdown(f"**Trivia:** {trivia}")
    
    # Reset option
    if st.button("Reset Game"):
        st.session_state["player_name"] = None
        st.session_state["progress"] = 0
        st.session_state["badge"] = None
