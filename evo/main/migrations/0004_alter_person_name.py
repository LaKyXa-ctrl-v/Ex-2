# Generated by Django 3.2.11 on 2022-01-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_name_person_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=30, verbose_name="Им'я"),
        ),
    ]