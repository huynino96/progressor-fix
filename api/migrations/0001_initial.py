# Generated by Django 3.1.3 on 2020-11-24 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileAndFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.IntegerField()),
                ('folder', models.IntegerField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Programming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('javascript', models.IntegerField()),
                ('java', models.IntegerField()),
                ('python', models.IntegerField()),
                ('php', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]