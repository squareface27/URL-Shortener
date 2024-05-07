import requests
import os
import re
import pyperclip
import customtkinter as ctk
from dotenv import load_dotenv
from CTkMessagebox import CTkMessagebox
import sys

load_dotenv()
token = os.getenv("TOKEN")
group_guid = os.getenv("GROUP_GUID")

def init_app():
    app = ctk.CTk()
    app.title("URL Shortener")
    app.geometry("800x400")
    app.resizable(False, False)
    ctk.set_appearance_mode("dark")
    return app

def init_gui(app):
    url_label = ctk.CTkLabel(app, text="Enter the URL:", font=("Arial", 13), text_color="white")
    url_label.place(relx=0.5, rely=0.40, anchor="center")
    url_field = ctk.CTkEntry(app, width=200, placeholder_text="Paste your URL here...")
    url_field.place(relx=0.5, rely=0.52, anchor="center")
    url_shortener_button = ctk.CTkButton(app, width=80, height=30, text="Submit", font=("Arial", 13), bg_color="blue", text_color="white", command=lambda: shorten_url(url_field))
    url_shortener_button.place(relx=0.7, rely=0.52, anchor="center")

def shorten_url(url_field):
    url = url_field.get()
    regex = r"https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    if url == "":
        CTkMessagebox(message="Please enter a URL!", icon="cancel", option_1="Close")
    elif not re.match(regex, url):
        CTkMessagebox(message="Please enter a valid URL!", icon="cancel", option_1="Close")
    else:
        headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }
        data = f'{{"long_url": "{url}", "domain": "bit.ly", "group_guid": "{group_guid}"}}'
        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
        pyperclip.copy(response.json()["link"])
        CTkMessagebox(message="The URL has been shortened and copied to your clipboard!",icon="check", option_1="Close")
        url_field.delete()
    
    
if __name__ == "__main__":
    app = init_app()
    init_gui(app)
    app.mainloop()