import streamlit as st

def chatbot():
    st.title("Chatbot")
    user_input = st.text_input("Enter your message:")
    if user_input == "hi":
        st.write("Hello! How can I help you today?")
    elif user_input == "what is your name?":
        st.write("I am a chatbot created with Streamlit.")
    elif user_input == "what do you do?":
        st.write("I am here to assist you with any questions you may have.")
    else:
        st.write("I'm sorry, I don't understand what you mean.")

if __name__ == '__main__':
    chatbot()
