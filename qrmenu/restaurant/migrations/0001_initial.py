# Generated by Django 3.2.5 on 2021-07-24 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('logo', models.ImageField(upload_to='logos/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('overview', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='meals/')),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='restaurant.category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='restaurant',
            field=models.ManyToManyField(to='restaurant.Restaurant'),
        ),
    ]
