# Generated by Django 3.2.5 on 2022-12-06 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_introvidep'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='introvidep',
            new_name='introvideo',
        ),
    ]
