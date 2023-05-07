import speech_recognition as sr
import requests

url = "https://simple-chatgpt-api.p.rapidapi.com/ask"

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Bir kelime / cümle söyleyin:")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="tr-TR")
        print("Söylediğiniz mesaj: " + text)

        payload = { "question": text }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "6f49bac845msh584b8be3d0b6c24p1b29d0jsndac34818b55e",
            "X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.json())
    except sr.UnknownValueError:
        print("Anlaşılamayan ses")
    except sr.RequestError as e:
        print("Ses hizmeti çalışmıyor; {0}".format(e))
