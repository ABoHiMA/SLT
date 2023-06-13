# Generated by Django 4.2.1 on 2023-05-20 22:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUUIDModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('TextBox', models.CharField(max_length=99, null=True)),
                ('TranslationBox', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Slimgs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Images', models.ImageField(upload_to='Photos/%y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Txtbx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.CharField(max_length=3, null=True)),
                ('Image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Translations.slimgs')),
            ],
        ),
    ]
