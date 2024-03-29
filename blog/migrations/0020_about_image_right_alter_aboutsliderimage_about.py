# Generated by Django 4.1.3 on 2022-12-13 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_about_alter_booking_service_aboutsliderimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image_right',
            field=models.ImageField(null=True, upload_to='Image Right About'),
        ),
        migrations.AlterField(
            model_name='aboutsliderimage',
            name='about',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.about'),
        ),
    ]
