# Generated by Django 4.2.5 on 2023-09-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(max_length=100)),
                ('x_min', models.FloatField()),
                ('x_max', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
