from django.shortcuts import render
from django.http import HttpResponse
from gtts import gTTS
import os

def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if text:
            tts = gTTS(text=text, lang='ru')
            static_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')
            if not os.path.exists(static_dir):
                os.makedirs(static_dir)
            file_path = os.path.join(static_dir, 'speech.mp3')
            tts.save(file_path)
            return render(request, 'voice/speech.html', {'audio_url': '/static/speech.mp3'})
    return render(request, 'voice/index.html')
