# Generated by Django 4.1.5 on 2023-01-18 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0004_alter_imagemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colourmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clr_f', to='testapi.productmodel'),
        ),
    ]
