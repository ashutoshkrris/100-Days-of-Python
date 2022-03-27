from PyPDF2 import PdfFileReader
import requests
import urllib.parse


BASE_URL = "http://api.voicerss.org/"
LANGUAGE = "en-in"
SPEECH_VOICE = "Jai"

text = ''

with open("sample.pdf", "rb") as file:
    pdf_file = PdfFileReader(file)
    total_pages = pdf_file.getNumPages()
    for i in range(total_pages):
        page = pdf_file.getPage(i)
        text += page.extractText()


params = {
    "key": "b9152bcb890847d0940f2a66b3522662",
    "src": text,
    "hl": LANGUAGE,
    "v": SPEECH_VOICE
}

response = requests.request(
    "POST", BASE_URL, params=params)

if response.status_code == 200:
    with open("audio.wav", "bx",) as f:
        f.write(response.content)
