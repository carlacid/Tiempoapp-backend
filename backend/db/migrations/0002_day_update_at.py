# Generated by Django 2.2.7 on 2019-11-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='update_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Updated at'),
        ),
    ]