# Generated by Django 3.2.19 on 2023-06-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgs', models.ImageField(upload_to='pics')),
                ('hd', models.CharField(max_length=250)),
                ('para', models.TextField()),
            ],
        ),
    ]
