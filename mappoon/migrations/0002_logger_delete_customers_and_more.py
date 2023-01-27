# Generated by Django 4.1.4 on 2023-01-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappoon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('time_log', models.TimeField(help_text='enter the exact time')),
            ],
        ),
        migrations.DeleteModel(
            name='customers',
        ),
        migrations.RemoveField(
            model_name='menu_category',
            name='category_id',
        ),
        migrations.DeleteModel(
            name='menu',
        ),
        migrations.DeleteModel(
            name='menu_category',
        ),
    ]