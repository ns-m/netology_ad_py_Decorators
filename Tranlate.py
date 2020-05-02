import requests
from decorators.decorator import decorator

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"

@decorator('./logs/log2.txt')
def translate_to_file(file, lang, text):
    with open(file, 'r') as f:
        translate = f.read()

    resp_translate = requests.post(URL, params = {
                                    "key": "trnsl.1.1.20191128T170444Z.c56d359e1889b3b7.8fccca1aa4fe51ff1bb52de2213efc89f26608ff",
                                    "text": translate,
                                    "lang": lang})
    with open("./data_files/RU.txt", "a") as f:
        resp_translate = resp_translate.json()["text"]
        resp_translate = ' '.join(resp_translate)
        f.write(f"{text}: {resp_translate}\n")

translate_to_file("./data_files/DE.txt", "de-ru", "Translation from German")
translate_to_file("./data_files/ES.txt", "es-ru", "Translation from Spanish")
translate_to_file("./data_files/FR.txt", "fr-ru", "Translation from French")