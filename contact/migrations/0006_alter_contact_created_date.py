# Generated by Django 4.2.4 on 2023-09-01 14:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_contact_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]