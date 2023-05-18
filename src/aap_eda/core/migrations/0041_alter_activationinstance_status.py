# Generated by Django 3.2.18 on 2023-05-18 21:56

import aap_eda.core.enums
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_activation_ruleset_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationinstance',
            name='status',
            field=models.TextField(choices=[('starting', 'starting'), ('running', 'running'), ('pending', 'pending'), ('failed', 'failed'), ('stopping', 'stopping'), ('stopped', 'stopped'), ('completed', 'completed')], default=aap_eda.core.enums.ActivationStatus['PENDING']),
        ),
    ]