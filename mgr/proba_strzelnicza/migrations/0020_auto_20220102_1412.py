# Generated by Django 3.2.9 on 2022-01-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proba_strzelnicza', '0019_alter_pliki_zdjecie'),
    ]

    operations = [
        migrations.AddField(
            model_name='pliki',
            name='kamera_szybka',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='pliki',
            name='kamera_zwykla',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
