# Generated by Django 2.2.3 on 2019-09-28 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0030_grant_clr_prediction_curve'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='weighted_shuffle',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
