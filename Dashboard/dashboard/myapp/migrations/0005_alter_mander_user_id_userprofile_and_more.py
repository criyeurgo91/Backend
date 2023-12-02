# Generated by Django 4.2.7 on 2023-11-29 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_document_url_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mander',
            name='user_id_userProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='account_id_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.account'),
        ),
    ]
