# Generated by Django 3.2.9 on 2021-12-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proba_strzelnicza', '0004_probastrzelnicza_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probastrzelnicza',
            name='link',
            field=models.CharField(max_length=80),
        ),
    ]