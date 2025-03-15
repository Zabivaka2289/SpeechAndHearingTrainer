from django.contrib import admin
from .models import AudioText

@admin.register(AudioText)
class AudioTextAdmin(admin.ModelAdmin):
    list_display = ('text', 'audio_file', 'created_at')
    search_fields = ('text',)