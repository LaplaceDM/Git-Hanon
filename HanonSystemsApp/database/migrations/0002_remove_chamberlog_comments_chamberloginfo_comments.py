# Generated by Django 4.2.9 on 2024-03-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chamberlog',
            name='comments',
        ),
        migrations.AddField(
            model_name='chamberloginfo',
            name='comments',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
