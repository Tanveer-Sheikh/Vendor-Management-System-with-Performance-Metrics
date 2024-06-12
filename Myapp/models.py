from django.db import models

# Create your models here.

class Vendor(models.Model):
    vendorid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __int__(self):
        return self.vendorid

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateField()
    delivery_date = models.DateField()
    items = models.TextField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateField(null=True)
    acknowledgment_date = models.DateField(null=True)
    currentdeliverydate = models.DateField(null=True)
    def __str__(self):
        return self.po_number + "--" + str(self.vendor)



class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    def __str__(self):
        return f"{self.vendor.name} - {self.date}"