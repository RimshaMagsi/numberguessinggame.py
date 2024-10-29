import streamlit as st
import random

# Initialize session state
if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Title and Instructions
st.title("🎲 Number Guessing Game!")
st.write("Guess the number between 1 and 100.")

# User Input
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    submit_button = st.button("Submit Guess")

    if submit_button:
        st.session_state.attempts += 1
        if guess < st.session_state.target_number:
            st.write("🔼 Too low! Try again.")
        elif guess > st.session_state.target_number:
            st.write("🔽 Too high! Try again.")
        else:
            st.write(f"🎉 Correct! The number was {st.session_state.target_number}.")
            st.write(f"You guessed it in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True

# Restart Game
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
