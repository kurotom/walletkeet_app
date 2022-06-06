# Generated by Django 4.0 on 2022-01-23 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_mywallet'),
    ]

    operations = [
        migrations.CreateModel(
            name='operations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('walletID', models.IntegerField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('date', models.CharField(blank=True, max_length=27, null=True)),
                ('username', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_Operations', to='wallet.user')),
                ('walletName', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_Name', to='wallet.mywallet')),
            ],
            options={
                'verbose_name_plural': 'Operations',
            },
        ),
    ]