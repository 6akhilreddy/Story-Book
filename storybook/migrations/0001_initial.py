# Generated by Django 2.1.4 on 2018-12-09 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('brief', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
