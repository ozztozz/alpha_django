# Generated by Django 5.1.5 on 2025-01-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takim', '0002_haftalikantrenman_tur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='haftalikantrenman',
            old_name='saat',
            new_name='baslangic',
        ),
        migrations.AddField(
            model_name='haftalikantrenman',
            name='bitis',
            field=models.TimeField(null=True),
        ),
    ]
