# Generated by Django 3.2.9 on 2021-11-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='upload')),
                ('unite', models.IntegerField()),
            ],
        ),
    ]
