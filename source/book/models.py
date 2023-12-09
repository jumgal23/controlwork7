from django.db import models


status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Article(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Имя автора")
    email = models.EmailField(max_length=100, null=False, blank=False, verbose_name='Почта автора')
    text = models.CharField(max_length=3000, default='Неизвестный', verbose_name="текст записи")
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=50, verbose_name="Статус", choices=status_choices, default='active')

    def __str__(self):
        return f'{self.id}. {self.name}'
