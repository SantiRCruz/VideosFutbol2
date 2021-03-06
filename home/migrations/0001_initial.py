# Generated by Django 3.1.7 on 2021-04-10 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoCategoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEquipo', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imgEquipo')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imgJugador')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreVideo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('videoUrl', models.CharField(max_length=100)),
                ('videoArchivo', models.FileField(blank=True, null=True, upload_to='videos')),
                ('fechaPublicacion', models.DateTimeField(auto_now=True)),
                ('Equipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.equipo')),
                ('Jugador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.jugador')),
                ('categoria', models.ManyToManyField(blank=True, null=True, to='home.Categoria')),
            ],
        ),
    ]
