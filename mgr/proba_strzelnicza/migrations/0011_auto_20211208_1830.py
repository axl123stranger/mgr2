# Generated by Django 3.2.9 on 2021-12-08 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proba_strzelnicza', '0010_auto_20211208_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='czynniki',
            name='proby',
        ),
        migrations.AddField(
            model_name='probastrzelnicza',
            name='czynnik',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='proba_strzelnicza.czynniki'),
        ),
    ]
