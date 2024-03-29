# Generated by Django 4.1.3 on 2022-12-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_offers_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('book_date', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Booking',
            },
        ),
        migrations.AlterModelOptions(
            name='offers',
            options={'verbose_name': 'Offer', 'verbose_name_plural': 'Offers'},
        ),
        migrations.AlterModelOptions(
            name='options',
            options={'verbose_name': 'Option', 'verbose_name_plural': 'Options'},
        ),
    ]
