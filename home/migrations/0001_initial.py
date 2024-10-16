# Generated by Django 5.0.3 on 2024-10-15 07:38

import django.core.validators
import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='pdf/', validators=[django.core.validators.FileExtensionValidator(['pdf']), home.models.validate_pdf_extension])),
            ],
        ),
    ]
