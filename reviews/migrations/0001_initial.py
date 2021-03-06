# Generated by Django 2.2.3 on 2019-11-07 16:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default=True, max_length=32, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='Фамилия')),
                ('message', models.TextField(blank=True, default=None, max_length=512, null=True, verbose_name='Отзыв')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актуальность отзыва')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания отзыва')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата редактирования отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='ReviewImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='review_images/', verbose_name='Фотография клиента')),
                ('is_main', models.BooleanField(default=False, verbose_name='Аватарка')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активная?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки фото')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Дата ред-ия фото')),
                ('review', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.Review', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Фотография клиента',
                'verbose_name_plural': 'Фотографии клиентов',
            },
        ),
    ]
