# Generated by Django 4.1.3 on 2022-12-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_category_work_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='slug',
            field=models.SlugField(editable=False, null=True),
        ),
    ]