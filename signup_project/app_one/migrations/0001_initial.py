# Generated by Django 5.0.3 on 2024-03-30 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_register',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('sirName', models.CharField(max_length=100)),
                ('mobileNo', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('con_password', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
