# Generated by Django 4.1.7 on 2023-03-20 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug_app', '0010_alter_bug_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='description',
            field=models.TextField(max_length=5000),
        ),
    ]
