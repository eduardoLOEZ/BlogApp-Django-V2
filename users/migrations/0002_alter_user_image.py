# Generated by Django 4.1.2 on 2022-10-30 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='/pic.jpg', null=True, upload_to=''),
        ),
    ]
