from django.shortcuts import render
from django.http import HttpResponse
from gtts import gTTS
import os
import random

# Список слов для выбора
WORDS = ["яблоко", "банан", "вишня", "финик", "бузина", "инжир", "виноград"]

def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if not text:
            text = random.choice(WORDS)  # Выбираем случайное слово, если текст не указан
        tts = gTTS(text=text, lang='ru')
        static_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)
        file_path = os.path.join(static_dir, 'speech.mp3')
        tts.save(file_path)
        return render(request, 'voice/speech.html', {'audio_url': '/static/speech.mp3', 'text': text})
    return render(request, 'voice/index.html')
