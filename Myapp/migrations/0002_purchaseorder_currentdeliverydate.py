# Generated by Django 5.0.4 on 2024-06-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='currentdeliverydate',
            field=models.DateTimeField(null=True),
        ),
    ]
