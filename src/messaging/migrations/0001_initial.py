# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-28 15:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opening', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainmessage', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=120)),
                ('msgtype', models.CharField(choices=[('Inactive', 'Inactive'), ('Messaged', 'Messaged'), ('Rejected', 'Rejected'), ('Application', 'Application'), ('Offer', 'Offer'), ('Job In Progress', 'Job In Progress'), ('Completed', 'Completed'), ('Canceled', 'Canceled'), ('Reviewed', 'Reviewed')], default='Inactive', max_length=30)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
                ('parent_id', models.PositiveIntegerField(blank=True, null=True)),
                ('re_opening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opening.Opening')),
                ('senduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('touser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', 'title'],
            },
        ),
    ]
