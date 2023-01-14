from gtts import gTTS
import playsound
import os
import speech_recognition as sr

class speaker(object):
    def speak(text):
        
        print("🤖: " + text)
        tts = gTTS(text=text, lang='vi',slow=False)
        filename = 'voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
        
    def command():
        playsound.playsound("./sound/Ping.mp3", False)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("...")
            audio = r.record(source, duration=4)
        try:
            text = r.recognize_google(audio, language='vi')   
            print("🧑: " + text)
            
        except sr.UnknownValueError:
            speaker.speak("Xin lỗi tôi không nghe thấy bạn nói gì,bạn có thể nhập từ bàn phím")
            text = str(input("Mời bạn nhập: "))
        return text.lower()