# Generated by Django 3.1.3 on 2022-11-25 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('darajacifapp', '0002_blog_blog_intro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='pnumber',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='status',
        ),
    ]
