# Generated by Django 2.0.5 on 2019-08-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0001_initial'),
        ('users', '0003_auto_20190819_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='home_church',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='church.Church'),
        ),
    ]
