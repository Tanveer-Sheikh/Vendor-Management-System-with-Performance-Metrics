# Generated by Django 5.0.4 on 2024-06-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_purchaseorder_currentdeliverydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='acknowledgment_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='currentdeliverydate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_date',
            field=models.DateField(),
        ),
    ]