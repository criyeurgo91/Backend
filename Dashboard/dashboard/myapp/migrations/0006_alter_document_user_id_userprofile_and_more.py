# Generated by Django 4.2.7 on 2023-11-29 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_mander_user_id_userprofile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='user_id_userProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile'),
        ),
        migrations.AlterField(
            model_name='request',
            name='user_id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile'),
        ),
    ]
