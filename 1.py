import streamlit as st

# Story content
story_lines = [
    "On March 25th, during Holi, he proposed to me.",
    "I like him very much, more than words can say.",
    "I want to be with him forever, through every joy and every sorrow.",
    "He should never be sad, never and ever, because I will always be by his side.",
    "And to show how much I care, here is my heart for you... ❤️"
]

# Function to manage the story navigation
def display_story():
    if "index" not in st.session_state:
        st.session_state.index = 0

    # Display the current line of the story
    st.write(story_lines[st.session_state.index])

    # Next button
    if st.session_state.index < len(story_lines) - 1:
        if st.button("Next"):
            st.session_state.index += 1
            st.experimental_rerun()

    # Previous button
    if st.session_state.index > 0:
        if st.button("Previous"):
            st.session_state.index -= 1
            st.experimental_rerun()

# Title
st.title("Our Love Story")

# Call the function to display the story
display_story()
