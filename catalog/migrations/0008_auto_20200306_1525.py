# Generated by Django 3.0.2 on 2020-03-06 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20200306_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('set_book_as_returned', '可以还书'),)},
        ),
    ]
