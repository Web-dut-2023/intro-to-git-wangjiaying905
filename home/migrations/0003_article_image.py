# Generated by Django 3.2.7 on 2023-11-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20231126_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='标题照片'),
        ),
    ]
