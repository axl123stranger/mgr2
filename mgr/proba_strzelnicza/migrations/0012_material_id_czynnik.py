# Generated by Django 3.2.9 on 2021-12-08 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proba_strzelnicza', '0011_auto_20211208_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='id_czynnik',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='proba_strzelnicza.czynniki'),
        ),
    ]