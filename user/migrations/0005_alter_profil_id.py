# Generated by Django 4.1.2 on 2022-11-09 19:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profil_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
