# Generated by Django 3.1.5 on 2021-02-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smmarket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('price', models.IntegerField(max_length=10)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
