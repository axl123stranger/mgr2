# Generated by Django 3.2.9 on 2021-12-08 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proba_strzelnicza', '0008_probastrzelnicza_kamera_ir'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='probastrzelnicza',
            name='czynnik',
        ),
    ]
