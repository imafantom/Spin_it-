import streamlit as st
import random

# Extended Vocabulary List
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
    {"word_en": "score", "word_pl": "wynik", "sentence": "He scored a goal in the last minute."},
    {"word_en": "proud", "word_pl": "dumny", "sentence": "She takes pride in her achievements."},
    {"word_en": "achievement", "word_pl": "osiągnięcie", "sentence": "Winning the competition was a major achievement."},
    {"word_en": "willingness", "word_pl": "chęć", "sentence": "His willingness to help was appreciated."},
    {"word_en": "make up for", "word_pl": "nadrobić", "sentence": "She worked hard to make up for lost time."},
    {"word_en": "deteriorate", "word_pl": "pogorszyć się", "sentence": "The condition of the building has deteriorated over time."},
    {"word_en": "passing by", "word_pl": "przechodzenie obok", "sentence": "I waved at my friend who was passing by."},
    {"word_en": "grinder", "word_pl": "młynek", "sentence": "He used a coffee grinder to prepare fresh coffee."},
    {"word_en": "grind", "word_pl": "mielić", "sentence": "Grind the beans until they're fine."},
    {"word_en": "instant", "word_pl": "natychmiastowy", "sentence": "Instant noodles are a quick snack."},
    {"word_en": "powder", "word_pl": "proszek", "sentence": "Add the baking powder to the flour."},
    {"word_en": "make-up", "word_pl": "makijaż", "sentence": "She bought new make-up for the party."},
    {"word_en": "nail polish", "word_pl": "lakier do paznokci", "sentence": "She chose a red nail polish for the event."},
    {"word_en": "lipstick", "word_pl": "pomadka", "sentence": "Her bright red lipstick matched her dress."},
    {"word_en": "face powder", "word_pl": "puder do twarzy", "sentence": "The face powder gives her a smooth complexion."},
    {"word_en": "handle", "word_pl": "uchwyt", "sentence": "The door handle was broken."},
    {"word_en": "knob", "word_pl": "gałka", "sentence": "He turned the knob to open the door."},
    {"word_en": "drawer", "word_pl": "szuflada", "sentence": "I keep my socks in the top drawer."},
    {"word_en": "fragile", "word_pl": "delikatny", "sentence": "Handle the vase carefully, it's very fragile."},
    {"word_en": "label", "word_pl": "etykieta", "sentence": "Read the label for washing instructions."},
    {"word_en": "container", "word_pl": "pojemnik", "sentence": "Store the food in an airtight container."},
    {"word_en": "DIY", "word_pl": "zrób to sam", "sentence": "He enjoys DIY projects on weekends."},
    {"word_en": "date", "word_pl": "randka", "sentence": "They went on a blind date last Friday."},
    {"word_en": "go Dutch", "word_pl": "dzielić się kosztami", "sentence": "We decided to go Dutch and split the bill."},
    {"word_en": "storage", "word_pl": "magazynowanie", "sentence": "This device has a large storage capacity."},
    {"word_en": "comedy", "word_pl": "komedia", "sentence": "We watched a hilarious comedy last night."},
    {"word_en": "comedian", "word_pl": "komik", "sentence": "The comedian had everyone laughing."},
    {"word_en": "enclose", "word_pl": "załączyć", "sentence": "Please enclose your resume with the application."},
    {"word_en": "attach", "word_pl": "przyczepić", "sentence": "Attach the file to the email before sending."},
    {"word_en": "envelope", "word_pl": "koperta", "sentence": "The letter was sealed in an envelope."},
    {"word_en": "attachment", "word_pl": "załącznik", "sentence": "The email had a PDF attachment."},
    {"word_en": "the very best", "word_pl": "najlepszy z najlepszych", "sentence": "He gave the very best performance of the night."},
    {"word_en": "convenience", "word_pl": "wygoda", "sentence": "Online shopping offers great convenience."},
    {"word_en": "application", "word_pl": "wniosek", "sentence": "Submit your application before the deadline."},
    {"word_en": "install", "word_pl": "zainstalować", "sentence": "I need to install the new software on my laptop."},
    {"word_en": "rush", "word_pl": "pośpiech", "sentence": "He left in a rush and forgot his phone."},
    {"word_en": "fool", "word_pl": "głupiec", "sentence": "Only a fool would ignore this opportunity."},
    {"word_en": "afford", "word_pl": "stać na coś", "sentence": "Can you afford to buy a new car?"},
    {"word_en": "pension", "word_pl": "emerytura", "sentence": "She plans to retire and live on her pension."},
    {"word_en": "impression", "word_pl": "wrażenie", "sentence": "Her presentation made a good impression."},
    {"word_en": "overpay", "word_pl": "przepłacić", "sentence": "I think we overpaid for this house."},
    {"word_en": "routine", "word_pl": "rutyna", "sentence": "My morning routine includes exercise and coffee."},
    {"word_en": "bother", "word_pl": "kłopotać się", "sentence": "Don't bother with the details, I'll handle it."},
    {"word_en": "native", "word_pl": "rodzimy", "sentence": "She is a native speaker of Spanish."},
    {"word_en": "privacy", "word_pl": "prywatność", "sentence": "Respecting one's privacy is important."},
    {"word_en": "invasion", "word_pl": "inwazja", "sentence": "The invasion of privacy is a serious issue."},
]

# English grammar trivia
trivia_list = [
"Did you know? English has borrowed words from over 350 languages!",
"Fun fact: The letter 'e' is the most commonly used letter in the English language.",
"Did you know? There are more English words starting with the letter 's' than with any other letter.",
"Fun fact: The sentence 'The quick brown fox jumps over the lazy dog' uses every letter in the English alphabet.",
"Did you know? 'I' is the shortest and most frequently used English word.",
"Trivia: Shakespeare invented over 1,700 words in the English language.",
"Did you know? English is the official language of aviation worldwide.",
"Fun fact: The word 'set' has over 400 different meanings in the English language!",
"Did you know? The longest word in English has 189,819 letters and is the chemical name for the protein 'titin.'",
"Trivia: The Oxford English Dictionary contains more than 170,000 words in current use.",
"Did you know? Over 2 billion people speak English worldwide, either as a first or second language.",
"Fun fact: There are only two English words ending with 'gry' – 'angry' and 'hungry.'",
"Did you know? English has no grammatical gender for nouns, unlike many other languages.",
"Trivia: The word 'queue' has the same pronunciation even when the last four letters are removed.",
"Fun fact: The word 'alphabet' is a combination of the first two Greek letters: alpha and beta.",
"Did you know? English is the only major language that doesn’t have a word for the day after tomorrow.",
"Trivia: The word 'run' has the most definitions of any word in the English language.",
"Fun fact: The phrase 'it's raining cats and dogs' comes from 17th-century England when heavy rain washed stray animals from rooftops.",
"Did you know? The original name of the butterfly was 'flutterby.'",
"Trivia: The longest monosyllabic word in English is 'screeched.'",
"Fun fact: The word 'dreamt' is the only English word that ends in 'mt.'"
"Did you know? English is the language of the internet, with over 55% of all websites written in English.",
"Trivia: The English language grows by about one new word every two hours!",
"Fun fact: The phrase 'kick the bucket' originated from slaughterhouses where animals were hung on buckets before being killed.",
"Did you know? The dot over the letters 'i' and 'j' is called a 'tittle.'",
"Trivia: The term 'OK' is derived from a misspelling of 'all correct' as 'oll korrect.'",
"Fun fact: The word 'clue' originally meant a ball of yarn. It comes from Greek mythology and Theseus's quest to navigate the labyrinth.",
"Did you know? 'Facetious' and 'abstemious' are the only words in English that have all the vowels in order.",
"Trivia: 'Noon' was originally derived from the Latin word 'nona,' meaning 'ninth hour,' referring to 3 PM!",
"Fun fact: The English language has more exceptions than rules when it comes to grammar.",
"Did you know? The word 'girl' was originally used to refer to a young person of either gender.",
"Trivia: The word 'emoji' comes from the Japanese words 'e' (picture) and 'moji' (character).",
"Fun fact: English is one of the only languages without diacritical marks, such as accents or umlauts.",
"Did you know? The shortest war in history was fought between the British and the Sultanate of Zanzibar, lasting only 38 minutes.",
"Trivia: The phrase 'bite the bullet' comes from historical battlefield surgeries, where patients bit on a bullet to endure pain.",
]

# State Initialization
if "player_name" not in st.session_state:
    st.session_state["player_name"] = None
if "progress" not in st.session_state:
    st.session_state["progress"] = 0
if "seen_words" not in st.session_state:
    st.session_state["seen_words"] = []
if "quiz_pending" not in st.session_state:
    st.session_state["quiz_pending"] = False

# Visual Enhancements
st.image("https://via.placeholder.com/800x150.png?text=Spin+It!+Game", use_column_width=True)

# Player Name Input
if st.session_state["player_name"] is None:
    st.title("Welcome to Spin It!")
    name = st.text_input("Enter your name to begin:")
    if st.button("Start Game"):
        if name.strip():
            st.session_state["player_name"] = name
else:
    st.title(f"Welcome, {st.session_state['player_name']}!")
    st.subheader(f"Words mastered: {st.session_state['progress']}")

    # Word Spin Button
    if not st.session_state["quiz_pending"] and st.button("Spin it!"):
        # Select a random word
        choice = random.choice(vocabulary)
        if choice not in st.session_state["seen_words"]:
            st.session_state["seen_words"].append(choice)
        st.session_state["progress"] += 1

        # Display Word and Sentence
        st.subheader(f"{choice['word_en']} / {choice['word_pl']}")
        st.write(choice["sentence"])

        # Show Trivia Every 5 Words
        if st.session_state["progress"] % 5 == 0:
            st.info(random.choice(trivia_list))

        # Trigger Quiz Every 10 Words
        if st.session_state["progress"] % 10 == 0:
            st.session_state["quiz_pending"] = True

    # Quiz Section
    if st.session_state["quiz_pending"]:
        st.write("It's quiz time!")
        quiz_word = random.choice(st.session_state["seen_words"])
        options = [word["word_pl"] for word in st.session_state["seen_words"]]
        correct_answer = quiz_word["word_pl"]
        options = random.sample(options, k=min(len(options), 3))
        if correct_answer not in options:
            options[random.randint(0, len(options) - 1)] = correct_answer

        selected = st.radio(f"What is the translation of '{quiz_word['word_en']}'?", options)
        if st.button("Submit Answer"):
            if selected == correct_answer:
                st.success("Correct!")
            else:
                st.error(f"Incorrect! The correct answer is: {correct_answer}")
            st.session_state["quiz_pending"] = False

    # Reset Button
    if st.button("Reset Game"):
        st.session_state["player_name"] = None
        st.session_state["progress"] = 0
        st.session_state["seen_words"] = []
        st.session_state["quiz_pending"] = False
