# Generated by Django 4.1.3 on 2023-11-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpsManager', '0003_remove_satis_yolcular_satis_yolcu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='satis',
            name='satildi',
            field=models.BooleanField(default=False, verbose_name='Satıldı mı?'),
        ),
    ]
