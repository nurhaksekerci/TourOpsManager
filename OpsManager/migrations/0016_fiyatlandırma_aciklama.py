# Generated by Django 4.1.3 on 2023-11-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpsManager', '0015_alter_fiyatlandırma_islem'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiyatlandırma',
            name='aciklama',
            field=models.TextField(default='Beklemede', verbose_name='Açıklama'),
        ),
    ]
