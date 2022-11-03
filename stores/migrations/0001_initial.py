# Generated by Django 3.2.13 on 2022-11-03 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodtag_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Thematag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thematag_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('store_address', models.CharField(max_length=100)),
                ('store_grade', models.IntegerField(default=0)),
                ('store_tel', models.CharField(max_length=100)),
                ('store_x', models.CharField(default=0, max_length=100)),
                ('store_y', models.CharField(default=0, max_length=100)),
                ('store_url', models.CharField(max_length=100)),
                ('kakao_id', models.IntegerField(blank=True)),
                ('store_image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='stores/')),
                ('foodtag_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stores.foodtag')),
                ('store_liked', models.ManyToManyField(related_name='like_stores', to=settings.AUTH_USER_MODEL)),
                ('thematag_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stores.thematag')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
