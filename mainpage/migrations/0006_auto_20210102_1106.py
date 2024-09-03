# Generated by Django 2.2.6 on 2021-01-02 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_order_product_ki_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(default=0, max_length=100),
        ),
    ]