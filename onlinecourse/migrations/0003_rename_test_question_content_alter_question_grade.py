# Generated by Django 4.2.3 on 2023-08-29 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='test',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=50),
        ),
    ]