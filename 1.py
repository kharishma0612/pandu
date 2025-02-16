import streamlit as st

# Story content
story_lines = [
    "My man is sad and i can't see that 😟.",
    "On March 25th, sattu pandu  proposed to me.",
    "I like him very much, more than words can say.",
    "I want to be with him forever, through every joy and every sorrow.",
    "He should never be sad, never and ever, because I will always be by his side.",
    "And to show how much I care, here is my heart for you... ❤️"
]

# Initialize session state
if 'index' not in st.session_state:
    st.session_state.index = 0

# Function to display the story
def display_story():
    # Display the current line of the story
    st.write(story_lines[st.session_state.index])

    # Buttons to navigate the story
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.session_state.index > 0:
            if st.button("Previous"):
                st.session_state.index -= 1

    with col2:
        if st.session_state.index < len(story_lines) - 1:
            if st.button("Next"):
                st.session_state.index += 1

# Title
st.title("Our Love Story")

# Display the story
display_story()
