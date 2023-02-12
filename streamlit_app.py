import streamlit as st
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def chatbot():
    st.title("Chatbot")
    user_input = st.text_input("Itroduce tu mensaje:").lower()
    if "hola" in user_input:
        st.write("hola! Como puedo ayudarte?")
    elif "llamas" in user_input:
        st.write("me llamo pishita.")
    elif "hacer" in user_input:
        st.write("Estoy aquí para ayudarte con cualquier pregunta que puedas tener.")
    elif "informacion" in user_input:
        query = user_input.replace("informacion", "").strip()
        results = search_google(query)
        if not results:
            st.write("No he ehcntrado resultados.")
        else:
            st.write("aqui tienes lo que he encntrado en Google:")
            for result in results:
                st.write("- [{}]({})".format(result["title"], result["link"]))
    else:
        st.write("lo siento, parece que te pasa algo en la boca, habla bien.")

def search_google(query):
    results = []
    search_url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": UserAgent().random,
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    for g in soup.find_all("div", class_="r"):
        anchors = g.find_all("a")
        if anchors:
            link = anchors[0]["href"].split("/url?q=")[-1]
            title = g.find("h3").text
            item = {"title": title, "link": link}
            results.append(item)
    return results

if __name__ == '__main__':
    chatbot()
