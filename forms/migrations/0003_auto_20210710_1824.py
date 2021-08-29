# Generated by Django 3.0 on 2021-07-10 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='category',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='forms.Form'),
        ),
        migrations.AddField(
            model_name='formfield',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='position',
            field=models.PositiveSmallIntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=10),
        ),
        migrations.AddField(
            model_name='formfield',
            name='updated_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='formfieldresponse',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='formfieldresponse',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=10),
        ),
        migrations.AddField(
            model_name='formfieldresponse',
            name='updated_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]