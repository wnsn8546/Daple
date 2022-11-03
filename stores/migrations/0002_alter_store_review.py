# Generated by Django 3.2.13 on 2022-11-03 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='review',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='store_reviews', to='reviews.review'),
        ),
    ]
