# Generated by Django 5.0.4 on 2024-06-09 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model_Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_type', models.CharField(max_length=50)),
                ('query_title', models.CharField(max_length=50)),
                ('justify', models.CharField(max_length=50)),
            ],
        ),
    ]
