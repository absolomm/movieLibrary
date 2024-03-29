# Generated by Django 2.0.2 on 2019-06-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_Icon', models.ImageField(upload_to='images/')),
                ('Name', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=50)),
                ('Movie_File', models.FileField(upload_to='videos/')),
                ('Client', models.CharField(max_length=50)),
                ('Project_Manager', models.CharField(max_length=50)),
                ('Creation_Date', models.DateField(auto_now_add=True)),
                ('Modified_Date', models.DateField(auto_now=True)),
            ],
        ),
    ]
