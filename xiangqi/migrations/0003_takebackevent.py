# Generated by Django 3.0.7 on 2020-06-15 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xiangqi', '0002_move_event_set'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakebackEvent',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('xiangqi.gameevent',),
        ),
    ]
