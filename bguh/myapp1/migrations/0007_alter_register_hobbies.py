# Generated by Django 5.0.7 on 2024-10-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0006_alter_register_city_alter_register_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='hobbies',
            field=models.JSONField(max_length=52),
        ),
    ]