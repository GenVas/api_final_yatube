# Generated by Django 3.2.5 on 2021-07-30 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_alter_follow_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ['following']},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date']},
        ),
    ]
