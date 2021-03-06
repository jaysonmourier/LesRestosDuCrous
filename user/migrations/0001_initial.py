# Generated by Django 3.2.9 on 2021-11-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=30)),
                ('nom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255)),
                ('telephone', models.CharField(max_length=10)),
                ('adresse', models.CharField(max_length=30)),
                ('nbParts', models.CharField(choices=[('0', '0-3'), ('1', '4-14'), ('2', '15-25'), ('3', '25-64'), ('4', 'Plus de 65')], default='2', max_length=10)),
                ('motMairie', models.BooleanField()),
                ('carteDonnee', models.BooleanField()),
                ('presenceDistribution', models.BooleanField()),
                ('remarque', models.CharField(max_length=255)),
                ('validated', models.BooleanField(default=0)),
            ],
        ),
    ]
