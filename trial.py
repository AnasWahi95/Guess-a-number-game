import streamlit as st
import random

# Initialize session state
if "randomNum" not in st.session_state:
    st.session_state.randomNum = random.randint(1, 13)
    st.session_state.guessAttempt = 1
    st.session_state.game_over = False
    st.session_state.name = ""

st.title("🕹 Guess a Number Game")

# Ask for name
if st.session_state.name == "":
    name = st.text_input("Enter your name:")
    if st.button("Start Game"):
        if name.strip() != "":
            st.session_state.name = name
else:
    st.write(f"Welcome user {st.session_state.name} 😇")
    st.write("I am thinking of a number between 1 and 13 🧐")

    if not st.session_state.game_over:
        st.write(f"Attempt {st.session_state.guessAttempt} of 4")

        guess = st.number_input("Enter your guess:", min_value=1, max_value=13, step=1)

        if st.button("Submit Guess"):
            if guess == st.session_state.randomNum:
                st.success("🎊 Congratulations. Correct guess 🎊")
                st.write(f"You guessed the number in {st.session_state.guessAttempt} attempt(s).")
                st.session_state.game_over = True

            elif guess > st.session_state.randomNum:
                st.warning("Your guess is too HIGH ⬆️. Think smaller.")
                st.session_state.guessAttempt += 1

            else:
                st.warning("Your guess is too LOW ⬇️. Think bigger.")
                st.session_state.guessAttempt += 1

            if st.session_state.guessAttempt > 4 and not st.session_state.game_over:
                st.error("😔 GAME OVER 😔")
                st.write(f"The correct number was {st.session_state.randomNum} 💎")
                st.session_state.game_over = True

    if st.button("Restart Game"):
        st.session_state.randomNum = random.randint(1, 13)
        st.session_state.guessAttempt = 1
        st.session_state.game_over = False
        st.session_state.name = ""