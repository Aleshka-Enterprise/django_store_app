# Generated by Django 4.2.5 on 2023-09-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_email_is_verified_emailverification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='date_of_expiration',
            field=models.DateTimeField(verbose_name='Срок окончания действия кода'),
        ),
    ]