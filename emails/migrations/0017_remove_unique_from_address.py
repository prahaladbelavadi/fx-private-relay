# Generated by Django 2.2.13 on 2021-05-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0016_domainaddress_first_emailed_at_nullable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainaddress',
            name='address',
            field=models.CharField(max_length=64),
        ),
    ]