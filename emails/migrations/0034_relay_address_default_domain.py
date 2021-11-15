# Generated by Django 2.2.24 on 2021-11-10 22:15

from django.db import migrations, models
import emails.models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0033_profile_last_account_flagged'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relayaddress',
            name='domain',
            field=models.PositiveSmallIntegerField(choices=[(1, 'RELAY_FIREFOX_DOMAIN'), (2, 'MOZMAIL_DOMAIN')], default=emails.models.default_domain_numerical),
        ),
    ]