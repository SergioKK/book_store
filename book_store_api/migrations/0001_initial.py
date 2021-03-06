# Generated by Django 2.2.2 on 2019-06-27 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('review', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('en', 'english'), ('ru', 'russian'), ('de', 'german')], max_length=200)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('binding', models.CharField(choices=[('s', 'soft'), ('h', 'hard')], max_length=200)),
                ('iSBN', models.IntegerField(choices=[('en', '5'), ('ru', '2'), ('de', '43')])),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('purchased_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_status', models.CharField(choices=[('1', 'in progress'), ('2', 'done'), ('3', 'canceled')], max_length=200)),
                ('purchased_books', models.ManyToManyField(to='book_store_api.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('authors_birthday', models.DateTimeField(default=django.utils.timezone.now)),
                ('authors_key_words', models.CharField(max_length=200)),
                ('books_income', models.FloatField()),
            ],
        ),
    ]
