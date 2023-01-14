import pyaudio
import struct
import pvporcupine  # thư viện hỗ trợ từ khóa đánh thức trợ lý
from ai_function.reply import reply
from intentclassification.intent_classification import IntentClassifier
from ai_function.speaklisten import speaker
from ai_function.open_web_search import assistant_browser
from ai_function.open_app import localapp
from ai_function.datatime import assistant_time
from ai_function.weather import weather
from ai_function.notepad import note
from ai_function.func import function
from ai_function.wallper_desktop import change_wallper



class Assistant:

    def __init__(self, name):
        self.name = name

    def reply(self, text):

        intent = intentclassifier.predict(text)

        if intent == 'leaving':
            speaker.speak("Rất vui được phục vụ bạn.")
            quit()

        replies = {
            'greeting': reply,
            'insult': reply,
            'install': reply,
            'function': function.main,
            'open_app': localapp.main,
            'datatime': assistant_time.main,
            'open_in_browser': assistant_browser.main,
            'weather': weather.main,
            'wallper':change_wallper.main,
            'note': note.main
            
           
        }

        try:
            reply_func = replies[intent]
            if callable(reply_func):
                reply_func(text, intent)
        except KeyError:
            speaker.speak("Xin lỗi mình chưa đủ thông minh để giúp bạn😣😣")

    def main(self):
        print("...")
        self.porcupine = None
        pa = None
        audio_stream = None

        # key của thư viện pvporcupine
        access_key = "08RPO8infyitaLPnJPEfKTK3+l3Cc73mZB2JDtEIVz71RYJ9TOYk/Q=="
        self.porcupine = pvporcupine.create(
            access_key=access_key, keywords=[self.name])

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length)

        # listens for hotword
        while True:
            try:
                pcm = audio_stream.read(self.porcupine.frame_length)
                pcm = struct.unpack_from(
                    "h" * self.porcupine.frame_length, pcm)
            except:
                audio_stream = pa.open(
                    rate=self.porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=self.porcupine.frame_length)

            keyword_index = self.porcupine.process(pcm)

            if keyword_index >= 0:
                speaker.speak("Vâng, có mình đây!")

                if audio_stream is not None:
                    audio_stream.close()
                said = speaker.command()  # Listens for user input
                self.reply(said)

intentclassifier = IntentClassifier()
assistant = Assistant("hey siri")
assistant.main()
