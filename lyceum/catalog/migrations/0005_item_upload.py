# Generated by Django 4.0.3 on 2022-04-26 10:35

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='upload',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
