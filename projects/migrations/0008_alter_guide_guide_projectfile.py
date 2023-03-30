# Generated by Django 4.1.3 on 2023-02-21 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_projectimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='guide',
            field=models.FileField(blank=True, null=True, upload_to='documents'),
        ),
        migrations.CreateModel(
            name='Projectfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='documents')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='projects.project')),
            ],
        ),
    ]