# Generated by Django 3.0 on 2022-04-22 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_notice_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
