# Generated by Django 3.0 on 2022-04-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('block', models.CharField(max_length=1)),
                ('number', models.CharField(max_length=3)),
                ('u_type', models.CharField(max_length=10)),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
