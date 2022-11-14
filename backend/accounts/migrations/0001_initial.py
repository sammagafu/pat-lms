# Generated by Django 3.2.5 on 2022-11-13 06:05

import django.core.validators
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=254, verbose_name='Full name')),
                ('phone', models.CharField(help_text='Example +255714112233', max_length=14, unique=True, validators=[django.core.validators.RegexValidator('^(\\+\\d{1,3})?,?\\s?\\d{8,13}')], verbose_name='Phone Number')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_student', models.BooleanField(default=False)),
                ('is_tuitor', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('mctnumber', models.CharField(blank=True, max_length=50, null=True, verbose_name='MCT Number')),
                ('avatar', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='profile/images/%Y/%m/%d', verbose_name='Profile Image')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
