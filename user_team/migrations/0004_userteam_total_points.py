# Generated by Django 2.2.5 on 2020-04-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_team', '0003_remove_userplayer_user_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='userteam',
            name='total_points',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
