# Generated by Django 3.2.9 on 2021-12-06 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proba_strzelnicza', '0003_rename_kamera_ir_szybka_pliki_zdjecie'),
    ]

    operations = [
        migrations.AddField(
            model_name='probastrzelnicza',
            name='link',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='proba_strzelnicza.pliki'),
        ),
    ]
