# Generated by Django 4.2.7 on 2023-12-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_alter_fotografia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
    ]
