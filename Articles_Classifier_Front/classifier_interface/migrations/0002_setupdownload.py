# Generated by Django 3.2.6 on 2022-06-14 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier_interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetupDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.TimeField(verbose_name='hour to download')),
            ],
        ),
    ]