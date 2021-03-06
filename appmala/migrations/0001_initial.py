# Generated by Django 3.2.9 on 2021-11-21 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('bookmark_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('comment_content', models.CharField(max_length=500)),
                ('comment_date', models.DateTimeField()),
            ],
            options={
                'ordering': ['comment_date'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('rating', models.FloatField(max_length=20)),
                ('phone_num', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('rating', models.FloatField(max_length=20)),
                ('review_date', models.DateTimeField()),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appmala.store')),
            ],
            options={
                'ordering': ['review_date'],
            },
        ),
    ]
