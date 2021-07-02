# Generated by Django 3.2 on 2021-04-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
                ('birth', models.DateField()),
                ('gender', models.IntegerField(choices=[(0, '女'), (1, '男')])),
                ('is_married', models.IntegerField(choices=[(0, '未婚'), (1, '已婚')])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birth', models.DateField()),
                ('gender', models.IntegerField(choices=[(0, '女'), (1, '男')])),
                ('teachers', models.ManyToManyField(to='school.Teachers')),
            ],
        ),
    ]
