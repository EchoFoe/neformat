from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, default='Имя категории', verbose_name='Наименование категории')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'


class ProductStatus(models.Model):
    name = models.CharField(max_length=128, default='Статус', verbose_name='Статус товара')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Статус товара'
        verbose_name_plural = 'Статус товара'


class Product(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default='iPhone',
                            verbose_name='Наименование товара')
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, default=0,
                                verbose_name='Цена товара (RUB)')
    vendor_code = models.CharField(max_length=16, blank=True, null=True, default=None,
                                   verbose_name='Артикул товара')
    discount = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True, default=0,
                                   verbose_name='Скидка (%)')
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=True, on_delete=models.CASCADE,
                                 verbose_name='Категория товара')
    status = models.ForeignKey(ProductStatus, blank=True, null=True, default=True, on_delete=models.CASCADE,
                               verbose_name='Статус товара')
    memory = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, default='64',
                                 verbose_name='Память')
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Описание товара')
    is_active = models.BooleanField(default=True, verbose_name='Наличие')
    top_sales = models.BooleanField(default=False, verbose_name='Лучш. пр-жи')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    @property
    def Наименование(self):
        return truncatechars(self.name, 50)

    @property
    def Описание(self):
        return truncatechars(self.description, 30)

    @property
    def Память(self):
        return truncatechars(self.memory, 30)

    def __str__(self):
        return "%s (%s)" % (self.name, self.price)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                verbose_name='Товар')
    image = models.ImageField(upload_to='products_images/', verbose_name='Фотографии товара')
    is_main = models.BooleanField(default=False, verbose_name='Обложка товара')
    is_active = models.BooleanField(default=True, verbose_name='Активная?')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата загрузки фото')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия фото')

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография товара'
        verbose_name_plural = 'Фотографии товаров'
