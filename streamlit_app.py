from selenium import webdriver
from bs4 import BeautifulSoup

def chatbot():
    user_input = input("Enter your message:").lower()
    if "hi" in user_input:
        print("Hello! How can I help you today?")
    elif "name" in user_input:
        print("I am a chatbot created with Streamlit.")
    elif "do" in user_input:
        print("I am here to assist you with any questions you may have.")
    elif "information" in user_input:
        query = user_input.replace("information", "").strip()
        results = search_google(query)
        if not results:
            print("No results found.")
        else:
            print("Here's what I found on Google:")
            for result in results:
                print("- {} ({})".format(result["title"], result["link"]))
    else:
        print("I'm sorry, I don't understand what you mean.")

def search_google(query):
    results = []
    search_url = f"https://www.google.com/search?q={query}"
    driver = webdriver.Firefox()
    driver.get(search_url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for g in soup.find_all("div", class_="r"):
        anchors = g.find_all("a")
        if anchors:
            link = anchors[0]["href"].split("/url?q=")[-1]
            title = g.find("h3").text
            item = {"title": title, "link": link}
            results.append(item)
    driver.quit()
    return results

if __name__ == '__main__':
    chatbot()
