import streamlit as st
import random  # FIX: Import random module

# Set page configuration for a unique look
st.set_page_config(page_title="Number Guessing Adventure", page_icon="🎲", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        font-family: 'Arial', sans-serif;
        color: #2c3e50;
        text-align: center;
        font-size: 40px;
        text-shadow: 2px 2px 4px #bdc3c7;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        padding: 10px 20px;
        display: block;
        margin: auto;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    .sidebar .sidebar-content {
        background-color: #ecf0f1;
        border-radius: 10px;
    }
    .feedback {
        font-size: 20px;
        color: #e74c3c;
        text-align: center;
    }
    .attempts {
        font-size: 18px;
        color: #8e44ad;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title with unique styling
st.markdown('<div class="title">Number Guessing Adventure 🎲</div>', unsafe_allow_html=True)

# Function to start or reset the game
def reset_game():
    st.session_state.number = random.randint(1, 100)  # Default range: 1 to 100
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.message = ""

# Initialize session state variables if not already set
if 'number' not in st.session_state:
    reset_game()

# Sidebar for optional enhancements with styled header
st.sidebar.markdown("### ⚙️ Game Settings")
custom_range = st.sidebar.checkbox("Set Your Own Range", help="Choose a custom range for the number!")
if custom_range:
    min_range = st.sidebar.number_input("Minimum Value", value=1, help="Smallest possible number")
    max_range = st.sidebar.number_input("Maximum Value", value=100, help="Largest possible number")
    if max_range <= min_range:
        st.sidebar.error("Max must be greater than Min!")
    else:
        st.session_state.number = random.randint(min_range, max_range)

difficulty = st.sidebar.selectbox("Choose Difficulty", ["Easy (Unlimited)", "Medium (10 attempts)", "Hard (5 attempts)"], help="Set your challenge level!")
max_attempts = {"Easy (Unlimited)": float('inf'), "Medium (10 attempts)": 10, "Hard (5 attempts)": 5}[difficulty]

# Main game logic with styled layout
st.write(f"🔍 Guess a number between {1 if not custom_range else min_range} and {100 if not custom_range else max_range}", 
         help="The secret number lies in this range!")
with st.container():
    guess = st.number_input("Enter your guess", step=1, min_value=0, key="guess_input", help="Type your number here!")

    if st.button("Submit Guess", key="submit"):
        st.session_state.attempts += 1
        if guess < st.session_state.number:
            st.session_state.message = "⬇️ Too low! Try again."
        elif guess > st.session_state.number:
            st.session_state.message = "⬆️ Too high! Try again."
        else:
            st.session_state.message = f"🎉 Congratulations! You guessed {st.session_state.number} in {st.session_state.attempts} attempts!"
            st.session_state.game_over = True

        if st.session_state.attempts >= max_attempts and not st.session_state.game_over:
            st.session_state.message = f"💥 Game Over! The number was {st.session_state.number}. No attempts left."
            st.session_state.game_over = True

# Display feedback and attempts with unique styling
st.markdown(f'<div class="feedback">{st.session_state.message}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="attempts">Attempts: {st.session_state.attempts}</div>', unsafe_allow_html=True)

# Fun instructions at the bottom
st.markdown("---")
st.write("💡 **How to Play**: Guess the secret number and hit 'Submit Guess'. Tweak the settings on the left to make it your own adventure!")  
