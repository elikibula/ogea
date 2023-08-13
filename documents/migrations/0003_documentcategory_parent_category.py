# Generated by Django 4.2 on 2023-06-30 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_document_author_document_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentcategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='documents.documentcategory'),
        ),
    ]
