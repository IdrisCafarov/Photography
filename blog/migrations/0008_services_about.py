# Generated by Django 4.1.3 on 2022-12-08 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_services_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='about',
            field=models.TextField(null=True),
        ),
    ]