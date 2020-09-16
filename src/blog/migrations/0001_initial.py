# Generated by Django 2.2 on 2020-09-15 16:34

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
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=320)),
                ('post_summary', models.TextField(blank=True, verbose_name='Pre Video Content')),
                ('youtube_video_id', models.CharField(blank=True, max_length=20)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blog/')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='DRAFT: Click to make this post draft, unchecked for publish(default).')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
