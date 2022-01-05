# Generated by Django 4.0 on 2022-01-05 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('restfulapi', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='captcha',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('captcha', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
