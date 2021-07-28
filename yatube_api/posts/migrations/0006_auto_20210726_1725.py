# Generated by Django 3.2.5 on 2021-07-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_rename_commemtpost_commentpost'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follow',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='follower',
            new_name='user',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('following', 'user'), name='unique_follow'),
        ),
    ]