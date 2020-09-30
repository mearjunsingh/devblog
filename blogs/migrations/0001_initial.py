# Generated by Django 3.1.1 on 2020-09-26 19:12

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('slug', models.SlugField(unique=True)),
                ('meta', models.TextField()),
                ('thumb', models.URLField(blank=True, help_text='We do not support uploading files.', null=True, verbose_name='thumbnail')),
                ('content', ckeditor.fields.RichTextField()),
                ('published', models.BooleanField(default=True)),
                ('views', models.IntegerField(default=0, editable=False)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
