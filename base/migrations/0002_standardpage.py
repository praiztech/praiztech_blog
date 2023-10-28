# Generated by Django 4.2.6 on 2023-10-26 11:29

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(required=True)), ('heading_size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a heading size'), ('h2', 'H2'), ('h3', 'H3')], required=False))])), ('paragraph', wagtail.blocks.RichTextBlock(blank=True)), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt', wagtail.blocks.CharBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False))]))], blank=True, use_json_field=True, verbose_name='Page content')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]