# Generated by Django 4.2 on 2023-04-16 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="expense",
            old_name="time",
            new_name="date",
        ),
    ]
