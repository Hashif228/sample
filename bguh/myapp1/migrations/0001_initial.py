# Generated by Django 5.0.7 on 2024-09-26 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=52)),
                ('lastname', models.CharField(max_length=52)),
                ('dob', models.DateField(max_length=52)),
                ('gender', models.CharField(max_length=52)),
                ('email', models.CharField(max_length=52)),
                ('phone', models.CharField(max_length=52)),
                ('country', models.CharField(max_length=52)),
                ('state', models.CharField(max_length=52)),
                ('city', models.CharField(max_length=52)),
                ('hobbies', models.CharField(max_length=52)),
                ('avatar', models.FileField(upload_to='hi')),
            ],
        ),
    ]