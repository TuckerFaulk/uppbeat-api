# Generated by Django 3.2.18 on 2023-04-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='category',
            field=models.CharField(choices=[('Jazz', 'Jazz'), ('Rock', 'Rock'), ('Chill', 'Chill')], default='Jazz', max_length=32),
        ),
    ]