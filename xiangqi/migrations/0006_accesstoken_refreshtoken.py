# Generated by Django 2.2 on 2019-12-01 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xiangqi', '0005_auto_20191129_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('expires_at', models.DateTimeField()),
                ('token', models.CharField(max_length=255, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='xiangqi.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('expires_at', models.DateTimeField()),
                ('token', models.CharField(max_length=255, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='xiangqi.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]