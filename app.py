import streamlit as st
import requests
import os

# ✅ API Setup
API_KEY = os.environ['OPENROUTER_API_KEY']
MODEL = "nousresearch/hermes-2-pro-mistral"

# ✅ Session chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ✅ Chat function
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
            "You are a helpful assistant. Speak professionally, clearly, and naturally like ChatGPT. Avoid robotic tone and disclaimers."
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


# ✅ Set page config and header
st.set_page_config(page_title="Sweety AI", page_icon="💬", layout="wide")
st.markdown("<h1 style='text-align: center;'>Sweety AI Chat Assistant</h1>",
            unsafe_allow_html=True)
st.divider()

# ✅ INPUT using ChatGPT-style chat_input
prompt = st.chat_input("Type your question...")

# ✅ Add to chat and display
if prompt:
    st.session_state.chat_history.append({"role": "user", "text": prompt})
    with st.spinner("Sweety is typing..."):
        reply = chat_with_ai(prompt)
        st.session_state.chat_history.append({
            "role": "assistant",
            "text": reply
        })

# ✅ Show messages like ChatGPT
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["text"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["text"])
