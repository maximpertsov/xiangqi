# Generated by Django 3.0.7 on 2020-06-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xiangqi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='event_set',
            field=models.ManyToManyField(related_name='move_set', to='xiangqi.GameEvent'),
        ),
    ]
