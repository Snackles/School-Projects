# Generated by Django 3.0.3 on 2020-02-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('body', models.TextField()),
                ('postDate', models.DateTimeField(auto_now_add=True)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['postDate'],
            },
        ),
    ]
