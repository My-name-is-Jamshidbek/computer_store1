# Generated by Django 4.0.6 on 2023-05-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(default=0, upload_to='products/'),
            preserve_default=False,
        ),
    ]
