# Generated by Django 4.1.3 on 2023-02-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_guide_guide_projectfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfile',
            name='name',
            field=models.CharField(default='null', max_length=200, verbose_name='Nombre'),
        ),
    ]