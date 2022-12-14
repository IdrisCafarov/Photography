# Generated by Django 4.1.3 on 2022-12-08 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_services_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Why_Us_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('about', models.TextField()),
            ],
            options={
                'verbose_name': 'Why Choose us in detail',
                'verbose_name_plural': 'Why Choose us in detail',
            },
        ),
        migrations.CreateModel(
            name='Why_Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=100)),
                ('why', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.why_us_detail')),
            ],
            options={
                'verbose_name': 'Why Us Options in Detail',
                'verbose_name_plural': 'Why Us Options in Detail',
            },
        ),
    ]
