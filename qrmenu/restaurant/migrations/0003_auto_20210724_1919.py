# Generated by Django 3.2.5 on 2021-07-24 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_restaurant_logo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='meal',
            name='restaurant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='restaurant.restaurant'),
            preserve_default=False,
        ),
    ]
