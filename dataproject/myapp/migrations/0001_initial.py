# Generated by Django 3.1.1 on 2023-04-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(help_text='Employee ID', max_length=4, primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencenumber', models.CharField(help_text='reference number', max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
