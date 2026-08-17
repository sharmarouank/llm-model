from dotenv import load_dotenv

load_dotenv()
from langchain.chat_models import init_chat_model

model = init_chat_model( 
    model ="mistral-large-latest",
    temperature=0.8,
    max_tokens =200
)

print("mistral chatbot")
print("type your message or enter 0 to exit.\n")

while True:

    user_input = input("you: ")

    if user_input.strip() =="0":
        print("getout: exiting the chat...")
        break

    response = model.invoke(user_input)
    print("mistral:",response.content)
    print()
