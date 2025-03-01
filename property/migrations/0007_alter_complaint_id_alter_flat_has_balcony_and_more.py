# Generated by Django 4.2.19 on 2025-02-26 20:22

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20250226_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='has_balcony',
            field=models.BooleanField(blank=True, db_index=True, null=True, verbose_name='Наличие балкона'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owners_phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='RU', verbose_name='Нормализованный номер владельца'),
        ),
    ]
