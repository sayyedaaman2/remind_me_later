# Generated by Django 5.0.3 on 2024-03-11 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.TextField(max_length=50)),
                ('mobile_no', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
