# Generated by Django 3.1.7 on 2022-03-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_shortanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Family', models.CharField(max_length=100)),
                ('Code', models.CharField(max_length=100)),
            ],
        ),
    ]