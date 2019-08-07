from django.db import models
from django.utils import timezone
from django.template.defaultfilters import truncatechars

class Support(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True, verbose_name='Имя')
    phone = models.CharField(max_length=19, blank=True, null=True, default='8-999-999-9999', verbose_name='Номер телефона')
    email = models.EmailField(max_length=128, default='example@domain.com', verbose_name='Емейл')
    subject = models.CharField(max_length=64, blank=True, null=True, verbose_name='Тема обращения')
    message = models.TextField(max_length=256, blank=True, null=True, default=None, verbose_name='Текст сообщения')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата обращения')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата ред-ия записи')

    @property
    def Тема(self):
        return truncatechars(self.subject, 32)

    @property
    def Сообщение(self):
        return truncatechars(self.message, 32)

    def __str__(self):
        return "Обращение от: %s" % self.email

    class Meta:
        verbose_name = 'Обращение клиента'
        verbose_name_plural = 'Обращения клиентов'