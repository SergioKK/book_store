# Generated by Django 2.2.2 on 2019-06-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='purchased_books',
            field=models.ManyToManyField(related_name='sells', to='book_store_api.Book'),
        ),
    ]
