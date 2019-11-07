from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone


class Review(models.Model):
    first_name = models.CharField(max_length=32,  blank=True, null=True, default=True, verbose_name='Имя')
    last_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='Фамилия')
    message = models.TextField(max_length=2048, null=True, blank=True, default=None, verbose_name='Отзыв')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность отзыва')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания отзыва')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования отзыва')

    @property
    def Отзыв(self):
        return truncatechars(self.message, 70)

    def __str__(self):
        return "%s" % self.first_name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, blank=True, null=True, default=None, on_delete=models.CASCADE,
                               verbose_name='Клиент')
    image = models.ImageField(upload_to='review_images/', verbose_name='Фотография клиента')
    is_main = models.BooleanField(default=False, verbose_name='Аватарка')
    is_active = models.BooleanField(default=True, verbose_name='Активная?')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата загрузки фото')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия фото')

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография клиента'
        verbose_name_plural = 'Фотографии клиентов'