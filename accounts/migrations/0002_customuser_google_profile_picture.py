# Generated by Django 4.1.7 on 2023-03-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="google_profile_picture",
            field=models.URLField(blank=True, null=True),
        ),
    ]
