# Generated by Django 4.2.4 on 2023-09-22 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eskak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='username',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UserEntries',
        ),
    ]