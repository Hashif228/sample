# Generated by Django 5.0.7 on 2024-11-08 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0029_test_alter_register_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='fee',
            field=models.CharField(max_length=52, unique=True),
        ),
    ]