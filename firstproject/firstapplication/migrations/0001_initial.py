# Generated by Django 3.2 on 2021-04-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
    ]
