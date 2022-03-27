# Generated by Django 3.2.12 on 2022-03-27 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileImportErrors',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('record', models.CharField(max_length=250)),
                ('error', models.CharField(max_length=250)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_error', to='contacts.fileimport')),
            ],
            options={
                'verbose_name': 'File Import Error',
                'verbose_name_plural': 'Files Import Errors',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=250)),
                ('card', models.CharField(max_length=20)),
                ('franchise', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.AddConstraint(
            model_name='contact',
            constraint=models.UniqueConstraint(fields=('user', 'email'), name='unique_user_contact'),
        ),
    ]
