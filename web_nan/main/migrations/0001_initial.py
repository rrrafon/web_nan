# Generated by Django 2.0.6 on 2018-06-10 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mainInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150)),
                ('author_bio', models.CharField(max_length=1000)),
                ('author_linkedIn', models.CharField(max_length=1000)),
                ('author_facebook', models.CharField(max_length=1000)),
            ],
        ),
    ]
