# Generated by Django 4.2.7 on 2023-12-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_sport_alter_adherent_acte_naissance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adherent',
            name='etat',
            field=models.CharField(choices=[('A', 'Active'), ('N', 'Non payé'), ('S', 'suspendu')], default='Active', max_length=1, verbose_name='Etat'),
            preserve_default=False,
        ),
    ]