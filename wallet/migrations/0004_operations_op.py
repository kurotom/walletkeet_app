# Generated by Django 4.0 on 2022-01-23 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_operations'),
    ]

    operations = [
        migrations.AddField(
            model_name='operations',
            name='op',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
