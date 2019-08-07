from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from utils.main import disable_for_loaddata


class Status(models.Model):
    name = models.CharField(max_length=128, default='Статус', verbose_name='Статус заказа')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

class Order(models.Model):
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, verbose_name='Клиент')
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name='Сумма заказа')
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=True, verbose_name='Имя клиента')
    customer_email = models.EmailField(blank=True, null=True, default=True, verbose_name='Почта клиента')
    customer_phone = models.CharField(max_length=68, blank=True, null=True, default=True, verbose_name='Телефон клиента')
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name='Адрес клиента')
    comments = models.TextField(blank=True, null=True, default=None, verbose_name='Комментарий')
    Status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус заказа')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия заказа')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.Status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

@disable_for_loaddata
def order_post_save(sender, instance, created, **kwargs):
    pass

post_save.connect(order_post_save, sender=Order)

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Товар')
    nmb = models.IntegerField(default=True, verbose_name='Количество')
    price_per_item = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name='Цена за штуку')
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name='Сумма')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        print(self.nmb)
        self.total_price = int(self.nmb) * self.price_per_item
        super(ProductInOrder, self).save(*args, **kwargs)

@disable_for_loaddata
def product_in_order_post_save(sender, instance, created, **kwargs):

    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name='Ключ')
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Товар')
    nmb = models.IntegerField(default=True, verbose_name='Количество')
    price_per_item = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name='Цена за штуку')
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name='Сумма')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item

        self.total_price = int(self.nmb) * price_per_item
        super(ProductInBasket, self).save(*args, **kwargs)