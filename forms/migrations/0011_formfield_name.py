# Generated by Django 3.0 on 2021-08-29 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0010_auto_20210822_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]