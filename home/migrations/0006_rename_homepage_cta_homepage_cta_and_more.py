# Generated by Django 4.2.6 on 2023-10-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepage_homepage_cta_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='homepage_cta',
            new_name='cta',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='homepage_cta_link',
            new_name='cta_link',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='homepage_image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='homepage_text',
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=models.TextField(blank=True, help_text='Write an introduction for the blog', null=True),
        ),
    ]
