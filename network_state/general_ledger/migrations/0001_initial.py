# Generated by Django 4.0.5 on 2022-07-06 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=64)),
                ('amount', models.IntegerField()),
                ('direction', models.BooleanField()),
            ],
        ),
    ]
