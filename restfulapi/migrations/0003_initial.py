# Generated by Django 4.0 on 2021-12-29 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restfulapi', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
