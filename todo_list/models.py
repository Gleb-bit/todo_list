from django.db import models


class TodoList(models.Model):
    uuid = models.CharField('UUID', max_length=8, unique=True, editable=False)
    created = models.DateField('Дата создания', auto_now_add=True)
    body = models.TextField('Тело', max_length=2000)
    active = models.BooleanField('Актив', default=True)

    class Meta:
        verbose_name = 'Лист заметок'
        verbose_name_plural = 'Листы заметок'

    def __str__(self):
        return f'{self.uuid}'
