# Generated by Django 4.1.4 on 2022-12-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
