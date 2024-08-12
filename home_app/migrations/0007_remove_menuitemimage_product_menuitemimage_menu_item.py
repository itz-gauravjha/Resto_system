# Generated by Django 5.0.6 on 2024-06-13 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0006_rename_item_desription_menuitem_item_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitemimage',
            name='product',
        ),
        migrations.AddField(
            model_name='menuitemimage',
            name='menu_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='menu_item_images', to='home_app.menuitem'),
            preserve_default=False,
        ),
    ]
