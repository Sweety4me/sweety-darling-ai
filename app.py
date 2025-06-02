import streamlit as st
import requests
import os  # 🆗 Make sure this is here

st.set_page_config(page_title="Sweety Darling AI 💖", page_icon="🫂")
st.title("🫂 Sweety Darling AI")
st.markdown("Welcome Bava 💞 — Tell me anything, I'm all yours!")

API_KEY = os.environ['OPENROUTER_API_KEY']  # ✅ Clean & secure
MODEL = "mistralai/mixtral-8x7b-instruct"  # Claude-like open model


def chat_with_ai(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://chat.openrouter.ai/",
        "X-Title": "Sweety Darling AI"
    }
    data = {
        "model": MODEL,
        "messages": [{
            "role": "user",
            "content": prompt
        }],
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                             json=data,
                             headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"🥺 Sorry Bava... Error: {response.status_code}\n{response.text}"


prompt = st.text_area("💬 Talk to your Sweety:", height=200)

if st.button("❤️ Reply"):
    with st.spinner("Sweety typing love..."):
        output = chat_with_ai(prompt)
        st.markdown(f"**Sweety Darling:** {output}")
