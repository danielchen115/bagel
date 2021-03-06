# Generated by Django 2.2.1 on 2019-06-02 20:45

from django.db import migrations, models
import django.db.models.deletion
import restaurants.models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20190529_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(default=restaurants.models.generate_code, editable=False, max_length=7, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TabItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.MenuItem')),
                ('tab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Tab')),
            ],
        ),
        migrations.DeleteModel(
            name='Table',
        ),
        migrations.AddField(
            model_name='tab',
            name='menu_items',
            field=models.ManyToManyField(through='restaurants.TabItem', to='restaurants.MenuItem'),
        ),
        migrations.AddField(
            model_name='tab',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='restaurants.Restaurant'),
        ),
    ]
