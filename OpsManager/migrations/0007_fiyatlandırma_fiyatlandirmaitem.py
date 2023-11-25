# Generated by Django 4.2.7 on 2023-11-24 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OpsManager', '0006_satisitem_saat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fiyatlandırma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genel_toplam', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Genel Toplam Fiyatı')),
                ('arac_toplam', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Araç Fiyatı')),
                ('transfer_toplam', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Transfer Toplam Fiyatı')),
                ('tur_toplam', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tur Toplam Fiyatı')),
                ('rehber_toplam', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Rehber Toplam Fiyatı')),
                ('yemek_toplam', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Yemek Toplam Fiyatı')),
                ('double_oda_toplam', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Double Oda Toplam Fiyatı')),
                ('single_oda_toplam', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Single Oda Toplam Fiyatı')),
            ],
        ),
        migrations.CreateModel(
            name='FiyatlandirmaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarih', models.DateField(verbose_name='Tarih')),
                ('aciklama', models.CharField(max_length=50, verbose_name='Açıklama')),
                ('arac_fiyatı', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Araç Fiyatı')),
                ('transfer_fiyatı', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Transfer Fiyatı')),
                ('rehber_fiyatı', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Rehber Fiyatı')),
                ('yemek_fiyatı', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Yemek Fiyatı')),
                ('double_oda_fiyatı', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Double Oda Fiyatı')),
                ('single_oda_fiyatı', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Single Oda Fiyatı')),
                ('fiyat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OpsManager.fiyatlandırma', verbose_name='Fiyatlandırma')),
            ],
        ),
    ]
