# Generated by Django 4.1.7 on 2023-02-16 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug_app', '0003_alter_bug_options_rename_completed_bug_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='complete',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
