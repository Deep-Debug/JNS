# Generated by Django 3.0.7 on 2020-07-15 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('Complain_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('problem', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='media/pics')),
                ('address', models.TextField(max_length=1000)),
                ('zip', models.CharField(max_length=20)),
                ('ward', models.CharField(max_length=20)),
                ('solved', models.BooleanField(default=False)),
                ('unsolved', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'Complain',
            },
        ),
    ]
