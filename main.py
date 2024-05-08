import requests
import os
import re
import pyperclip
import customtkinter as ctk
from dotenv import load_dotenv
from CTkMessagebox import CTkMessagebox
import json

load_dotenv()
token = os.getenv("TOKEN")
group_guid = os.getenv("GROUP_GUID")

def load_language(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def init_app():
    app = ctk.CTk()
    app.title(translations['app']['title'])
    app.geometry("800x400")
    app.resizable(False, False)
    ctk.set_appearance_mode("dark")
    return app

def init_gui(app):
    url_label = ctk.CTkLabel(app, text=translations['main_form']['url_label'], font=("Arial", 13), text_color="white")
    url_label.place(relx=0.5, rely=0.40, anchor="center")
    url_field = ctk.CTkEntry(app, width=200, placeholder_text=translations['main_form']['url_field'])
    url_field.place(relx=0.5, rely=0.52, anchor="center")
    url_shortener_button = ctk.CTkButton(app, width=80, height=30, text=translations['button']['submit'], font=("Arial", 13), bg_color="blue", text_color="white", command=lambda: shorten_url(url_field))
    url_shortener_button.place(relx=0.7, rely=0.52, anchor="center")

def shorten_url(url_field):
    url = url_field.get()
    regex = r"https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    if url == "":
        CTkMessagebox(message=translations['error']['missing_url'], icon="cancel", option_1=translations['button']['close'])
    elif not re.match(regex, url):
        CTkMessagebox(message=translations['error']['invalid_url'], icon="cancel", option_1=translations['button']['close'])
    else:
        headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }
        data = f'{{"long_url": "{url}", "domain": "bit.ly", "group_guid": "{group_guid}"}}'
        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
        pyperclip.copy(response.json()["link"])
        CTkMessagebox(message=translations['main_form']['successful_message'],icon="check", option_1=translations['button']['close'])
        url_field.delete(0, 'end')
    
    
if __name__ == "__main__":
    language = 'en'
    translations = load_language(f'locales/{language}.json')
    app = init_app()
    init_gui(app)
    app.mainloop()