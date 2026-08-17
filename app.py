import streamlit as st

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    model = "mistral-small-latest",
    temperature = 0.8,
    max_tokens = 200
)

st.title("🤖 Mistral Chatbot")
st.write("Chat with Mistral AI")

user_input = st.chat_input("Type your message...")

if user_input:
    response = model.invoke(user_input)

    st.write("You:", user_input)
    st.write("Mistral:", response.content)
    