# Generated by Django 3.0.2 on 2020-03-06 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200306_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('a b c', 'Set book as returned'),)},
        ),
    ]
