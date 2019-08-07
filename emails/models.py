from django.db import models
from django.utils import timezone

class EmailType(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Тип эл. адреса')
    is_active = models.BooleanField(default=True, verbose_name='Акутальность')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тип е-мейла'
        verbose_name_plural = 'Типы е-мейлов'

class EmailSendingFact (models.Model):
    type = models.ForeignKey(EmailType, on_delete=models.CASCADE, verbose_name='Тип эл. адреса')
    order = models.ForeignKey('orders.Order', blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Заказ')
    email = models.EmailField(max_length=128, verbose_name='Электронный адрес')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата отправки')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return self.type.name

    class Meta:
        verbose_name = 'Отправленный е-мейл'
        verbose_name_plural = 'Отправленные е-мейлы'


