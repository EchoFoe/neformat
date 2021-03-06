# Generated by Django 2.2.3 on 2019-08-03 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0007_auto_20190803_1931'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Сумма заказа')),
                ('customer_name', models.CharField(blank=True, default=True, max_length=128, null=True, verbose_name='Имя клиента')),
                ('customer_email', models.EmailField(blank=True, default=True, max_length=254, null=True, verbose_name='Почта клиента')),
                ('customer_phone', models.CharField(blank=True, default=True, max_length=68, null=True, verbose_name='Телефон клиента')),
                ('customer_address', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Адрес клиента')),
                ('comments', models.TextField(blank=True, default=None, null=True, verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата созд-ия заказа')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Дата ред-ия записи')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Статус', max_length=128, verbose_name='Статус заказа')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актуальность')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата созд-ия записи')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Дата ред-ия записи')),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'verbose_name_plural': 'Статусы заказов',
            },
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmb', models.IntegerField(default=True, verbose_name='Количество')),
                ('price_per_item', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Цена за штуку')),
                ('total_price', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Сумма')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актуальность')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата созд-ия записи')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Дата ред-ия записи')),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Заказ')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказе',
            },
        ),
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Ключ')),
                ('nmb', models.IntegerField(default=True, verbose_name='Количество')),
                ('price_per_item', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Цена за штуку')),
                ('total_price', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Сумма')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актуальность')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата созд-ия записи')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Дата ред-ия записи')),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Заказ')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='Status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Status', verbose_name='Статус заказа'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
    ]
