# Generated by Django 5.0.2 on 2024-06-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_promo_name_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='name',
            field=models.CharField(default='', max_length=20, verbose_name='Имя'),
            preserve_default=False,
        ),
    ]
