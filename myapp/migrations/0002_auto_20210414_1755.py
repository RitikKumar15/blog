# Generated by Django 3.1.7 on 2021-04-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='desc',
            field=models.CharField(max_length=200),
        ),
    ]
