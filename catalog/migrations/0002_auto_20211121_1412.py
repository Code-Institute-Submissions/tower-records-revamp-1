# Generated by Django 3.2.9 on 2021-11-21 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storeproduct',
            options={'ordering': ('-created_on',), 'verbose_name_plural': 'Products'},
        ),
        migrations.RenameField(
            model_name='storeproduct',
            old_name='date_created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='storeproduct',
            old_name='product_instock',
            new_name='product_in_stock',
        ),
        migrations.RenameField(
            model_name='storeproduct',
            old_name='product_isactive',
            new_name='product_is_active',
        ),
        migrations.RenameField(
            model_name='storeproduct',
            old_name='date_updated',
            new_name='updated_on',
        ),
    ]
