from django.shortcuts import render
from django.http import HttpResponse
from gtts import gTTS
import os
import random
from datetime import datetime  # Для работы с датой и временем
from .models import AudioText  # Импортируем модель

# Список слов для выбора
WORDS = ["яблоко", "банан", "вишня", "финик", "бузина", "инжир", "виноград"]

def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if not text:
            text = random.choice(WORDS)  # Выбираем случайное слово, если текст не указан
        
        # Генерация уникального имени файла
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Формат: ГГГГММДД_ЧЧММСС
        file_name = f"speech_{timestamp}.mp3"
        
        # Создание пути для сохранения файла
        static_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)
        file_path = os.path.join(static_dir, file_name)

        # Генерация аудиофайла
        tts = gTTS(text=text, lang='ru')
        tts.save(file_path)

        # Сохранение данных в БД
        audio_text_instance = AudioText(
            text=text,
            audio_file=f"/static/{file_name}"  # Сохраняем путь к файлу
        )
        audio_text_instance.save()

        return render(request, 'voice/speech.html', {
            'audio_url': f'/static/{file_name}',
            'text': text
        })
    
    return render(request, 'voice/index.html')