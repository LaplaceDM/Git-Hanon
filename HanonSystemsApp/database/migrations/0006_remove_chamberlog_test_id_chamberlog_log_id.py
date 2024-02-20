# Generated by Django 4.2.9 on 2024-02-14 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_chamberloginfo_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chamberlog',
            name='test_id',
        ),
        migrations.AddField(
            model_name='chamberlog',
            name='log_id',
            field=models.ForeignKey(db_column='log_id', default=4, on_delete=django.db.models.deletion.CASCADE, to='database.chamberloginfo'),
            preserve_default=False,
        ),
    ]