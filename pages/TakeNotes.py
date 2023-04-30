import streamlit as st

st.title('Notes...')
st.divider()

import streamlit as st

# Check if 'text' already exists in session_state
# If not, then initialize it with an empty string
if 'text' not in st.session_state:
    st.session_state['text'] = ''

# Display a text area widget with the value from session_state
notes_prompt = st.text_area("Type in here", value=st.session_state.text)

# Update the value of 'text' in session_state with the current value of the text area widget
st.session_state.text = notes_prompt

st.download_button("Download", notes_prompt, "text.txt")
