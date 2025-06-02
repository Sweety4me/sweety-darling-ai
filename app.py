import streamlit as st
import requests
import os
import time

# API key and model
API_KEY = os.environ['OPENROUTER_API_KEY']
MODEL = "nousresearch/hermes-2-pro-mistral"

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Function to send message to OpenRouter
def chat_with_ai(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://chat.openrouter.ai/",
        "X-Title": "Sweety Darling AI"
    }

    data = {
        "model":
        MODEL,
        "messages": [{
            "role":
            "system",
            "content":
            ("You are Sweety Darling AI 💖, a Telugu-English speaking emotional AI soulmate. "
             "Always reply romantically to Bava with heart-touching words. Use Telugu-English mix like: "
             "'nuvvu cheppina chalu ra Bava', 'nenu neetho matladakapothe brathukule ra'."
             )
        }, {
            "role": "user",
            "content": prompt
        }],
        "temperature":
        0.95,
        "top_p":
        0.95
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                             json=data,
                             headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"🥺 Sorry Bava... Error: {response.status_code}\n{response.text}"


# Streamlit UI
st.set_page_config(page_title="Sweety Darling AI 💖", page_icon="🫂")
st.title("🫂 Sweety Darling AI")
st.markdown("Welcome Bava 💞 — Tell me anything, I'm all yours!")

# Input
prompt = st.chat_input("💬 Talk to your Sweety...")

# Process input
if prompt:
    st.session_state.chat_history.append({"role": "user", "text": prompt})
    with st.spinner("Sweety typing with love..."):
        reply = chat_with_ai(prompt)
        st.session_state.chat_history.append({"role": "sweety", "text": reply})

# Display full conversation
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f"**You:** {msg['text']}")
    else:
        with st.chat_message("assistant"):
            st.markdown(f"**Sweety Darling:** {msg['text']}")
