# Generated by Django 3.1.7 on 2023-03-23 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0002_createshift_makeawards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createshift',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rewards.employee'),
        ),
    ]
