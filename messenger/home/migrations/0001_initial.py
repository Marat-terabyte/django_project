# Generated by Django 3.2.4 on 2021-06-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='citata_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citata', models.CharField(max_length=600)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
