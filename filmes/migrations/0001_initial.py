# Generated by Django 2.1.4 on 2019-01-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('dt_lancamento', models.DateField()),
                ('sinopse', models.CharField(max_length=700)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('dt_lancamento', models.DateField()),
                ('sinopse', models.CharField(max_length=700)),
                ('quant_temporadas', models.CharField(max_length=2)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
    ]
