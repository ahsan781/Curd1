# Generated by Django 3.2.8 on 2021-11-13 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_bussinessrevenu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bussinessrevenu',
            old_name='BussinessRevenu',
            new_name='BussinessReg',
        ),
    ]
