# Generated by Django 4.0 on 2022-01-05 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('restfulapi', '0004_captcha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captcha',
            name='id',
            field=models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user'),
        ),
    ]
