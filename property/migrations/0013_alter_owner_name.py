# Generated by Django 4.2.19 on 2025-03-01 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_move_owners_to_new_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
    ]
