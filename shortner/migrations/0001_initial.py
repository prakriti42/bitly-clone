# Generated by Django 3.2.5 on 2021-08-28 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputUrl', models.CharField(max_length=13000)),
                ('urlid', models.CharField(max_length=6)),
            ],
        ),
    ]
