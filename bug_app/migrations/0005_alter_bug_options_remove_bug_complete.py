# Generated by Django 4.1.7 on 2023-02-16 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bug_app', '0004_alter_bug_complete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bug',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='bug',
            name='complete',
        ),
    ]
