# Generated by Django 2.2 on 2022-02-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
            ],
        ),
    ]
