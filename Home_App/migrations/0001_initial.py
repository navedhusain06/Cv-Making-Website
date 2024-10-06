# Generated by Django 5.1.1 on 2024-09-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cvTemplateClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='IMAGE')),
                ('contactNumber', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('socialMediaLinks', models.CharField(max_length=200)),
                ('languages', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('education', models.TextField()),
                ('experience', models.TextField()),
            ],
        ),
    ]
