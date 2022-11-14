# Generated by Django 3.2.5 on 2022-11-13 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProuctCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=160)),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
            options={
                'verbose_name': 'Course Category',
                'verbose_name_plural': 'Courses Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategoryname', models.CharField(max_length=160)),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='coursecategory.prouctcategory', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Course Sub-Category',
                'verbose_name_plural': 'Courses Sub-Categories',
            },
        ),
    ]
