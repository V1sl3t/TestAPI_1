from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Advertisement(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=200)
    views_number = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-position']
