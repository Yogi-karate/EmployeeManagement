# Generated by Django 3.1.1 on 2020-09-07 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0003_auto_20200907_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee_register.position'),
        ),
    ]
