from django.db import models

class AudioText(models.Model):
    text = models.CharField(max_length=255, verbose_name="Текст")
    audio_file = models.FileField(upload_to='audio/', verbose_name="Аудиофайл", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Аудио и текст"
        verbose_name_plural = "Аудио и тексты"