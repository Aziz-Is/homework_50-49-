# Generated by Django 4.0.6 on 2022-07-14 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_status_status_alter_type_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(default='new', max_length=20),
        ),
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(default='task', max_length=20),
        ),
    ]