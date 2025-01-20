# Generated by Django 5.1.3 on 2024-12-02 19:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterField(
            model_name='antrenor',
            name='ozet',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='antrenor',
            name='ozgecmis',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='metin',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='resim',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
