# Generated by Django 4.0.1 on 2022-02-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('longitude', models.IntegerField()),
                ('latitude', models.IntegerField()),
                ('claimedBy', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('possession', models.IntegerField()),
            ],
        ),
    ]
