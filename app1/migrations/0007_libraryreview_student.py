# Generated by Django 5.1.1 on 2024-12-14 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_libraryreview_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryreview',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.student'),
            preserve_default=False,
        ),
    ]
