import json
from ai_function.determine_most_similar import determine_most_similar_phrase
from ai_function.speaklisten import speaker
import random

def reply(text, intent):
    with open(f'./samples/{intent}.json',encoding='utf-8') as samplesfile:  
        samples = json.load(samplesfile)
    most_similar = determine_most_similar_phrase(text = text, intent_dict = samples)

    if type(samples[most_similar]) == str:
        speaker.speak(samples[most_similar])
    elif type(samples[most_similar]) == list:
         speaker.speak(random.choice(samples[most_similar]))
