# Generated by Django 2.0.5 on 2019-04-30 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Remote_User', '0006_review_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertweets_model',
            name='uname',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
