# Generated by Django 3.1.5 on 2021-01-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=256)),
                ('year', models.IntegerField(null=True)),
                ('genres', models.ManyToManyField(db_table='movie_genre', related_name='movies', to='recoflix.Genre')),
            ],
        ),
    ]