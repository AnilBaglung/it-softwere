# Generated by Django 4.0.2 on 2022-02-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_servic_description_servic_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servic',
            name='description',
            field=models.TextField(max_length=10000),
        ),
    ]
