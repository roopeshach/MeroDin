# Generated by Django 3.2.5 on 2021-07-21 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Routine', '0002_auto_20210722_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='name',
            field=models.CharField(default='ok', max_length=200),
            preserve_default=False,
        ),
    ]