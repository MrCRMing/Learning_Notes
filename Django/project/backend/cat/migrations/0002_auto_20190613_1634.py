# Generated by Django 2.0 on 2019-06-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='mood',
            field=models.CharField(choices=[(('HAY',), 'happy'), (('GRY',), 'grumpy'), (('BAD',), 'bad')], default=('HAY',), max_length=3),
        ),
    ]
