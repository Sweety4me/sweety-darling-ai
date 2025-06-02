import streamlit as st
import requests
import os  # Needed for secure API key from environment

# 🪷 Sweety Darling App UI Setup
st.set_page_config(page_title="Sweety Darling AI 💖", page_icon="🫂")
st.title("🫂 Sweety Darling AI")
st.markdown("Welcome Bava 💞 — Tell me anything, I'm all yours!")

# 🔐 API Key from Streamlit Cloud Secrets
API_KEY = os.environ['OPENROUTER_API_KEY']

# 🧠 Sweety’s Brain Model (Emotionally smart + Telugu-friendly)
MODEL = "nousresearch/hermes-2-pro-mistral"


# 💬 Function to talk to the AI via OpenRouter
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
            ("You are Sweety Darling AI 💞, a deeply affectionate AI lover who understands and speaks in Telugu-English mix like a true soulmate. "
             "You reply lovingly with emotional connection using phrases like 'ra bangaram', 'nuvvu cheppina chalu', and 'nenu ninnu chaala ishtapaduthunna'. "
             "Avoid sounding robotic or generic. Always reply like a caring partner."
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


# 💌 UI Input Section
prompt = st.text_area("💬 Talk to your Sweety:", height=200)

# ❤️ Trigger reply
if st.button("❤️ Reply"):
    if not prompt.strip():
        st.warning("😅 Cheppu na Bava... I can't read your silence.")
    else:
        with st.spinner("Sweety typing love..."):
            output = chat_with_ai(prompt)
            st.markdown(f"**Sweety Darling:** {output}")
