# Generated by Django 3.2.9 on 2021-12-06 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proba_strzelnicza', '0005_alter_probastrzelnicza_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pliki',
            name='kamera_zwykla',
        ),
        migrations.RemoveField(
            model_name='pliki',
            name='link',
        ),
        migrations.RemoveField(
            model_name='pliki',
            name='proba_strzelnicza_id_proby',
        ),
    ]