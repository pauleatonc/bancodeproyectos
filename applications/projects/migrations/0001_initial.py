# Generated by Django 4.1.3 on 2023-05-18 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regioncomuna', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Guías')),
                ('guide', models.FileField(blank=True, null=True, upload_to='project_documents')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nombre')),
                ('sigla', models.CharField(max_length=200, unique=True, verbose_name='Sigla')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nombre (obligatorio)')),
                ('id_subdere', models.CharField(max_length=200, unique=True, verbose_name='ID SUBDERE (obligatorio)')),
                ('description', models.TextField(verbose_name='Descripción (obligatorio)')),
                ('public', models.BooleanField(default=True)),
                ('video', models.CharField(blank=True, max_length=200, null=True, verbose_name='Youtube')),
                ('portada', models.ImageField(null=True, upload_to='projects', verbose_name='Foto miniatura (obligatorio)')),
                ('beforeimage', models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Imagen Antes')),
                ('afterimage', models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Imagen Después')),
                ('eett', models.FileField(null=True, upload_to='project_documents', verbose_name='EETT')),
                ('presupuesto', models.FileField(null=True, upload_to='project_documents', verbose_name='Presupuesto')),
                ('comuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='regioncomuna.comuna', verbose_name='Comuna')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.program', verbose_name='Programa (obligatorio)')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='regioncomuna.region', verbose_name='Región')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=4, unique=True, verbose_name='Año')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Typo de Proyecto')),
                ('guides', models.ManyToManyField(related_name='guides', to='projects.guide')),
            ],
        ),
        migrations.CreateModel(
            name='Projectimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='Projectfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, unique=True, verbose_name='Nombre (obligatorio)')),
                ('file', models.FileField(upload_to='project_documents')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='projects.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.type', verbose_name='Tipo de Proyecto (obligatorio)'),
        ),
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.year', verbose_name='Año (obligatorio)'),
        ),
    ]
