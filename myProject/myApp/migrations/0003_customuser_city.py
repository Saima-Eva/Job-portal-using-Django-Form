# Generated by Django 5.0.1 on 2024-01-31 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_customuser_user_type_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
