# Generated by Django 4.0.3 on 2022-05-26 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_question_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
    ]
