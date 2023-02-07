from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

class Todo(models.Model):
    name = models.CharField(max_length=127, verbose_name='Названия')
    description = models.TextField(verbose_name='Описнаие')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(verbose_name='Дата рождения')
    image = models.ImageField(
        upload_to='todp/image/', verbose_name='Картинка'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='todoes', verbose_name='Пользователь'
    )
    is_done = models.BooleanField(
        default=False, verbose_name='Готов ли?'
    )

    def __str__(self):
        return self.name
    

