# Generated by Django 4.2.3 on 2023-08-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver_id',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_id',
            field=models.CharField(),
        ),
    ]
