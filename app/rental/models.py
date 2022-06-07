from django.db import models


class Car(models.Model):
    """Car model"""

    name = models.CharField('Название', max_length=50)
    create_year = models.PositiveIntegerField('Год выпуска')
    add_date = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['name', 'add_date']

    def __str__(self):
        return self.name
