# Generated by Django 4.1.7 on 2023-03-31 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0004_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='cartid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.cart'),
        ),
    ]