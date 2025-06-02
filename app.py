import streamlit as st
import requests
import os

# API key and model
API_KEY = os.environ['OPENROUTER_API_KEY']
MODEL = "nousresearch/hermes-2-pro-mistral"

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Function to call OpenRouter
def chat_with_ai(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://chat.openrouter.ai/",
        "X-Title": "Sweety AI"
    }

    data = {
        "model":
        MODEL,
        "messages": [{
            "role":
            "system",
            "content":
            "You are a helpful, intelligent assistant who answers clearly and naturally. Avoid robotic tone. Respond like a human with professionalism and clarity. Avoid disclaimers."
        }, {
            "role": "user",
            "content": prompt
        }],
        "temperature":
        0.9,
        "top_p":
        0.95
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                             json=data,
                             headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"


# Page config
st.set_page_config(page_title="Sweety AI", page_icon="💬", layout="wide")

# Header
st.markdown("<h2 style='text-align: center;'>Sweety AI Chat Assistant</h2>",
            unsafe_allow_html=True)
st.divider()

# Chat input
user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "text": user_input})
    with st.spinner("Thinking..."):
        reply = chat_with_ai(user_input)
        st.session_state.chat_history.append({
            "role": "assistant",
            "text": reply
        })

# Chat history display
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["text"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["text"])
