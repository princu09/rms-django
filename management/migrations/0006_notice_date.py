# Generated by Django 3.0 on 2022-04-22 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20220422_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
