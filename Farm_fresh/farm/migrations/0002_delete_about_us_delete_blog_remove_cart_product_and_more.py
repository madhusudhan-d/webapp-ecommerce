# Generated by Django 4.2.2 on 2023-06-19 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About_us',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='username',
        ),
        migrations.DeleteModel(
            name='Contact_us',
        ),
        migrations.DeleteModel(
            name='Enquiry',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]