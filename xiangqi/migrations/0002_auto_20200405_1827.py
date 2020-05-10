# Generated by Django 2.2 on 2020-04-05 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xiangqi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='xiangqi.Player'),
        ),
        migrations.AlterField(
            model_name='game',
            name='black_player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='xiangqi.Player'),
        ),
        migrations.AlterField(
            model_name='game',
            name='red_player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='xiangqi.Player'),
        ),
        migrations.AlterField(
            model_name='move',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xiangqi.Player'),
        ),
        migrations.AlterField(
            model_name='refreshtoken',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='xiangqi.Player'),
        ),
    ]