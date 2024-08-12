# Generated by Django 5.0.6 on 2024-06-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=55)),
                ('number', models.IntegerField()),
                ('date', models.DateField()),
                ('person', models.IntegerField()),
            ],
        ),
    ]
