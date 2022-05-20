import requests
import urllib.request
import os

if not os.path.exists("files"):
    os.mkdir("files")

def download_img(url, path=""):
    path = path if path else url.split("/")[-1]
    r = requests.get(url)
    open("files/" + path, 'wb').write(r.content)

def download_text(url, path=""):
    path = path if path else url.split("/")[-1]
    r = urllib.request.urlopen(url)
    open("files/" + path, 'w').write(r.read().decode('utf-8'))

download_img("https://www.facebook.com/favicon.ico")
download_text("https://raw.githubusercontent.com/Fisherman386/Sample-Text-Creator/76067bab4d68ac5322a2b91b42cccd960ab160e2/languages.json","langs.json")