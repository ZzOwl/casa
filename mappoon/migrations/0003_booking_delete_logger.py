# Generated by Django 4.1.4 on 2023-01-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappoon', '0002_logger_delete_customers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('guest_count', models.IntegerField()),
                ('reservation_time', models.DateField(auto_now=True)),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Logger',
        ),
    ]