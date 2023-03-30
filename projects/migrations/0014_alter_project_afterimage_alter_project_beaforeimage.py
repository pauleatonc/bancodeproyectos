# Generated by Django 4.1.3 on 2023-03-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_project_afterimage_project_beaforeimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='afterimage',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Imagen Después'),
        ),
        migrations.AlterField(
            model_name='project',
            name='beaforeimage',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Imagen Antes'),
        ),
    ]