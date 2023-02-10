from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Task(models.Model):
    title = models.CharField(verbose_name="Pavadinimas", max_length=100)
    description = models.TextField(verbose_name="Aprašymas", max_length=500)
    user = models.ForeignKey(to=User, verbose_name="Vartotojas", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Sukūrimo data", auto_now_add=True)
    due = models.DateField(verbose_name="Padaryti iki")

    ORDER_STATUS = (
            ('p', 'Padaryta'),
            ('n', 'Nepradėta'),
            ('v', 'Vykdoma')
        )

    status = models.CharField(verbose_name='Statusas', max_length=1, choices=ORDER_STATUS, help_text='Parinkite užduoties būklę', default='n')

    def is_overdue(self):
        return self.due and date.today() > self.due

    def __str__(self):
        return f"Užduotis: {self.title} - ({self.date})"

    class Meta:
        verbose_name = 'Užduotis'
        verbose_name_plural = 'Užduotys'
        ordering = ['-date']
