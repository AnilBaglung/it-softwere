# Generated by Django 4.0.2 on 2022-02-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_kada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
