# Generated by Django 5.1.1 on 2024-12-13 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_student_std_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='std_id',
        ),
    ]