import streamlit as st
import requests
from bs4 import BeautifulSoup

def chatbot():
    st.title("Chatbot")
    user_input = st.text_input("Enter your message:").lower()
    if "hi" in user_input:
        st.write("Hello! How can I help you today?")
    elif "name" in user_input:
        st.write("I am a chatbot created with Streamlit.")
    elif "do" in user_input:
        st.write("I am here to assist you with any questions you may have.")
    elif "information" in user_input:
        query = user_input.replace("information", "").strip()
        results = search_google(query)
        st.write("Here's what I found on Google:")
        for result in results:
            st.write("- [{}]({})".format(result["title"], result["link"]))
    else:
        st.write("I'm sorry, I don't understand what you mean.")

def search_google(query):
    results = []
    search_url = "https://www.google.com/search?q={}".format(query)
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")
    for g in soup.find_all("div", class_="r"):
        anchors = g.find_all("a")
        if anchors:
            link = anchors[0]["href"]
            title = g.find("h3").text
            item = {"title": title, "link": link}
            results.append(item)
    return results

if __name__ == '__main__':
    chatbot()
