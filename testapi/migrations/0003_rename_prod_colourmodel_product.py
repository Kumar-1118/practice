# Generated by Django 4.1.5 on 2023-01-12 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0002_alter_imagemodel_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colourmodel',
            old_name='prod',
            new_name='product',
        ),
    ]