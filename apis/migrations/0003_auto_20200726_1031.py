# Generated by Django 3.0.8 on 2020-07-26 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_task_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='modified',
            new_name='modified_at',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]