# Generated by Django 4.0.3 on 2022-04-05 20:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docTitle', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]