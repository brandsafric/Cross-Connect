# Generated by Django 2.0.5 on 2019-08-21 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('time', models.TimeField()),
                ('day', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=1)),
                ('church', models.ForeignKey(on_delete='CASCADE', to='church.Church')),
            ],
        ),
    ]
