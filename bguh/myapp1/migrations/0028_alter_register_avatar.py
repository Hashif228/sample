# Generated by Django 5.0.7 on 2024-10-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0027_alter_register_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='avatar',
            field=models.ImageField(default='static\\img\x05star.png', max_length=52, upload_to='files/'),
        ),
    ]
