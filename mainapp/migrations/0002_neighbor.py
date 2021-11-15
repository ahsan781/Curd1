# Generated by Django 3.2.9 on 2021-11-09 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Neighborname', models.CharField(max_length=200)),
                ('subDistrict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.subdistrict')),
            ],
        ),
    ]
