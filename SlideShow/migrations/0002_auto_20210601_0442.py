# Generated by Django 3.2.3 on 2021-06-01 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SlideShow', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thumbnall',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
