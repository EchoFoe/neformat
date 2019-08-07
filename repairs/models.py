from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone


class RepairCategory(models.Model):
    name = models.CharField(max_length=128, default='Услуга', verbose_name='Наименование услуги')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Услуга по ремонту'
        verbose_name_plural = 'Услуги по ремонтам'


class Repair(models.Model):
    iphone_4 = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                   verbose_name='iPhone 4/4s')
    iphone_5 = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                   verbose_name='iPhone 5/5c')
    iphone_5s = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                    verbose_name='iPhone 5s')
    iphone_6 = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                   verbose_name='iPhone 6')
    iphone_6_plus = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                        verbose_name='iPhone 6+')
    iphone_6s = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                    verbose_name='iPhone 6s')
    iphone_6s_plus = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                         verbose_name='iPhone 6s+')
    iphone_se = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                    verbose_name='iPhone SE')
    iphone_7 = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                   verbose_name='iPhone 7')
    iphone_7_plus = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                        verbose_name='iPhone 7+')
    iphone_8 = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                   verbose_name='iPhone 8')
    iphone_8_plus = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                        verbose_name='iPhone 8+')
    iphone_x = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                   verbose_name='iPhone X')
    iphone_xr = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                    verbose_name='iPhone Xr')
    iphone_xs = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                    verbose_name='iPhone Xs')
    iphone_xs_max = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True, default=None,
                                        verbose_name='iPhone Xs Max')
    category = models.ForeignKey(RepairCategory, blank=True, null=True, default=True, on_delete=models.CASCADE,
                                 verbose_name='УСЛУГА')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "%s:" % self.category

    class Meta:
        verbose_name = 'Цена на услугу'
        verbose_name_plural = 'Цены на услуги'


class RepairImage(models.Model):
    repair = models.ForeignKey(Repair, blank=True, null=True, default=None, on_delete=models.CASCADE,
                               verbose_name='Услуга')
    image = models.ImageField(upload_to='repairs_images/', verbose_name='Фотографии услуг')
    is_main = models.BooleanField(default=False, verbose_name='Обложка услуги')
    is_active = models.BooleanField(default=True, verbose_name='Активная?')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата загрузки фото')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия фото')

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография услуги'
        verbose_name_plural = 'Фотографии услуг'

class Statement(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True, verbose_name='Имя')
    phone = models.CharField(max_length=19, blank=True, null=True, default='8-999-999-9999', verbose_name='Номер телефона')
    email = models.EmailField(max_length=128, default='example@domain.com', verbose_name='Емейл')
    message = models.TextField(max_length=256, blank=True, null=True, default=None, verbose_name='Текст сообщения')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата обращения')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата ред-ия записи')

    @property
    def Сообщение(self):
        return truncatechars(self.message, 32)

    def __str__(self):
        return "Обращение от: %s" % self.email

    class Meta:
        verbose_name = 'Заявка на ремонт'
        verbose_name_plural = 'Заявки на ремонт'