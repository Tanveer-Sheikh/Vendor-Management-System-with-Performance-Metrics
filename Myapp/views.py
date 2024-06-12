from rest_framework import serializers
from .models import Vendor, PurchaseOrder,HistoricalPerformance
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime


def createVendor(request, vendor_id=None):
    if request.method == "GET":
      
        data = {}
        if(vendor_id==None):
            vendors = Vendor.objects.all()
            for vendor in vendors:
                data[vendor.vendorid] = {
                    'name': vendor.name,
                    'contact_details': vendor.contact_details,
                    'address': vendor.address,
                    'vendor_code': vendor.vendor_code,
                    'on_time_delivery_rate': vendor.on_time_delivery_rate,
                    'quality_rating_avg': vendor.quality_rating_avg,
                    'average_response_time': vendor.average_response_time,
                    'fulfillment_rate': vendor.fulfillment_rate
                }
        else:
            vendor = Vendor.objects.get(pk=vendor_id)
            data = {
                'id': vendor.vendorid,
                'name': vendor.name,
                'contact_details': vendor.contact_details,
                'address': vendor.address,
                'vendor_code': vendor.vendor_code,
                'on_time_delivery_rate': vendor.on_time_delivery_rate,
                'quality_rating_avg': vendor.quality_rating_avg,
                'average_response_time': vendor.average_response_time,
                'fulfillment_rate': vendor.fulfillment_rate
            }
      
        return JsonResponse({'data': data}, status=201)
 
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')
        contact_details = data.get('contact_details')
        address = data.get('address')
        vendor_code = data.get('vendor_code')
        on_time_delivery_rate = data.get('on_time_delivery_rate')
        quality_rating_avg = data.get('quality_rating_avg')
        average_response_time = data.get('average_response_time')
        fulfillment_rate = data.get('fulfillment_rate')

        if not name or not vendor_code:
                return JsonResponse({'error': 'Name and vendor code are required'}, status=400)
        else:
            vendor = Vendor.objects.create(
                name=name,
                contact_details=contact_details,
                address=address,
                vendor_code=vendor_code,
                on_time_delivery_rate=on_time_delivery_rate,
                quality_rating_avg=quality_rating_avg,
                average_response_time=average_response_time,
                fulfillment_rate=fulfillment_rate
            )
            print(vendor)
            historical_performance_data(vendor.vendorid,on_time_delivery_rate,quality_rating_avg,average_response_time,fulfillment_rate)
            return JsonResponse({'data': 'Vendpor Created'}, status=201)

    if request.method == "DELETE":
      
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            vendor.delete()
            return JsonResponse({'Data': 'Vendor Deleted'}, status=201)
        except Vendor.DoesNotExist:
            return JsonResponse({'error': 'Vendor not found'}, status=404)

    if request.method == "PUT":
        vendor = Vendor.objects.get(pk=vendor_id)
        try:
          
            data = json.loads(request.body)
            name = data.get('name')
            contact_details = data.get('contact_details')
            address = data.get('address')
            vendor_code = data.get('vendor_code')
            on_time_delivery_rate = data.get('on_time_delivery_rate')
            quality_rating_avg = data.get('quality_rating_avg')
            average_response_time = data.get('average_response_time')
            fulfillment_rate = data.get('fulfillment_rate')
                
            vendor.name = name
            vendor.contact_details = contact_details
            vendor.address = address
            vendor.vendor_code = vendor_code
            vendor.on_time_delivery_rate = on_time_delivery_rate
            vendor.quality_rating_avg = quality_rating_avg
            vendor.average_response_time = average_response_time
            vendor.fulfillment_rate = fulfillment_rate
            
            vendor.save()
            
            return JsonResponse({'Updated': 'Vendor Updated found'}, status=201)
       
                
        except Vendor.DoesNotExist:
                return JsonResponse({'error': 'Vendor not found'}, status=404)


    return JsonResponse({'error': 'Method not allowed'}, status=405)


def purchaseOrder(request,po_number=None):
    
    if request.method == "GET":
        data = {}
        if(po_number == None):
            orders = PurchaseOrder.objects.all()
            
            for order in orders:
                
                data[order.po_number] = {
                    'po_number': order.po_number,
                    'vendor_id': order.vendor_id,
                    'order_date': order.order_date,
                    'delivery_date': order.delivery_date,
                    'items': order.items,
                    'quantity': order.quantity,
                    'status': order.status,
                    'quality_rating': order.quality_rating,
                    'issue_date': order.issue_date,
                    'acknowledgment_date': order.acknowledgment_date
                }
        else:
            purchase_order = PurchaseOrder.objects.get(po_number=po_number)
            
            data = {
                'po_number': purchase_order.po_number,
                'vendor_id': purchase_order.vendor_id,
                'order_date': purchase_order.order_date,
                'delivery_date': purchase_order.delivery_date,
                'items': purchase_order.items,
                'quantity': purchase_order.quantity,
                'status': purchase_order.status,
                'quality_rating': purchase_order.quality_rating,
                'issue_date': purchase_order.issue_date,
                'acknowledgment_date': purchase_order.acknowledgment_date
            }
        return JsonResponse(data)
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            po_number = data.get('po_number')
            vendor_id = data.get('vendor_id')
            order_date = data.get('order_date')
            delivery_date = data.get('delivery_date')
            items = data.get('items')
            quantity = data.get('quantity')
            status = data.get('status')
            quality_rating = data.get('quality_rating')
            issue_date = data.get('issue_date')
            acknowledgment_date = None
            if not po_number or not vendor_id:
                return JsonResponse({'error': 'PO number and vendor ID are required'}, status=400)

            order = PurchaseOrder.objects.create(
                po_number=po_number,
                vendor_id=vendor_id,
                order_date=order_date,
                delivery_date=delivery_date,
                items=items,
                quantity=quantity,
                status=status,
                quality_rating=quality_rating,
                issue_date=issue_date,
                acknowledgment_date=acknowledgment_date,
                
            )

            return JsonResponse({'message': 'Purchase order created successfully'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON payload'}, status=400)

    if request.method == "DELETE":
        try:
            purchase_order = PurchaseOrder.objects.get(po_number=po_number)
            
            purchase_order.delete()

            return JsonResponse({'message': 'Purchase order deleted successfully'})

        except PurchaseOrder.DoesNotExist:
            return JsonResponse({'error': 'Purchase order not found'}, status=404)
    if request.method == "PUT":
        try:
            purchase_order = PurchaseOrder.objects.get(po_number=po_number)
            request_data = json.loads(request.body)

            purchase_order.po_number = request_data.get('po_number', purchase_order.po_number)
            purchase_order.vendor_id = request_data.get('vendor_id', purchase_order.vendor_id)
            purchase_order.order_date = request_data.get('order_date', purchase_order.order_date)
            purchase_order.delivery_date = request_data.get('delivery_date', purchase_order.delivery_date)
            purchase_order.items = request_data.get('items', purchase_order.items)
            purchase_order.quantity = request_data.get('quantity', purchase_order.quantity)
            purchase_order.status = request_data.get('status', purchase_order.status)
            purchase_order.quality_rating = request_data.get('quality_rating', purchase_order.quality_rating)
            purchase_order.issue_date = request_data.get('issue_date', purchase_order.issue_date)
            purchase_order.acknowledgment_date = request_data.get('acknowledgment_date', purchase_order.acknowledgment_date)

            if(request_data.get('status')=="completed"):
                purchase_order.currentdeliverydate = datetime.now()
            purchase_order.save()

            if(request_data.get('status')=="completed"):
                update_vendor_performance(purchase_order.vendor_id)

            
                

            return JsonResponse({'message': 'Purchase order updated successfully'})

        except PurchaseOrder.DoesNotExist:
            return JsonResponse({'error': 'Purchase order not found'}, status=404)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def acknowledge_po(request, po_number=None):
    try:
        order = PurchaseOrder.objects.get(po_number=po_number)
        order.status = "Ack"
        order.acknowledgment_date = datetime.now()
        order.save()
        update_vendor_performance(order.vendor_id)
        return JsonResponse({'data': 'Acknowledged'}, status=200)
    except PurchaseOrder.DoesNotExist:
        return JsonResponse({'error': 'Purchase order not found'}, status=404)

def perfomance(request,vendor_id):
    vendor = Vendor.objects.get(pk=vendor_id)
    data = {
        'id': vendor.vendorid,
        'name': vendor.name,
        'contact_details': vendor.contact_details,
        'address': vendor.address,
        'vendor_code': vendor.vendor_code,
        'on_time_delivery_rate': vendor.on_time_delivery_rate,
        'quality_rating_avg': vendor.quality_rating_avg,
        'average_response_time': vendor.average_response_time,
        'fulfillment_rate': vendor.fulfillment_rate
    
    }
    return JsonResponse({'data': data}, status=201)


def update_vendor_performance(vendor_id):
    on_time_delivery_rate(vendor_id)
    quality_rating_average(vendor_id)
    average_response_time(vendor_id)
    fulfillment_rate(vendor_id)
    vendor = Vendor.objects.get(vendorid=vendor_id)
    historical_performance_data(vendor.vendorid, vendor.on_time_delivery_rate, vendor.quality_rating_avg, vendor.average_response_time, vendor.fulfillment_rate)



def on_time_delivery_rate(vendor_id):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor_id, status="completed")
    on_time_count = sum(compare_dates(str(order.delivery_date),str( order.delivery_date)) for order in completed_orders)
    vendor = Vendor.objects.get(vendorid=vendor_id)
    vendor.on_time_delivery_rate = on_time_count / (1 if len(completed_orders) == 0 else len(completed_orders))
    vendor.save()
  

def quality_rating_average(vendor_id):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor_id, status="completed")
    total_quality_rating = sum(order.quality_rating for order in completed_orders)
    vendor = Vendor.objects.get(vendorid=vendor_id)
    vendor.quality_rating_avg = total_quality_rating /  (1 if len(completed_orders) == 0 else len(completed_orders))
    vendor.save()
    

def average_response_time(vendor_id):
    orders = PurchaseOrder.objects.filter(vendor=vendor_id)
    total_response_time = sum(difference_dates(str(order.issue_date),str( order.acknowledgment_date)) for order in orders if order.acknowledgment_date and order.issue_date)
    vendor = Vendor.objects.get(vendorid=vendor_id)
    vendor.average_response_time = total_response_time / (1 if len(orders) == 0 else len(orders))
    vendor.save()
   

def fulfillment_rate(vendor_id):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor_id, status="completed")
    issued_orders_count = sum(1 for order in completed_orders if order.issue_date)
    vendor = Vendor.objects.get(vendorid=vendor_id)
    vendor.fulfillment_rate = issued_orders_count / (1 if len(completed_orders) == 0 else len(completed_orders))
    vendor.save()
   

def historical_performance_data(vendor_id, on_time_delivery_rate, quality_rating_avg, average_response_time, fulfillment_rate):
    HistoricalPerformance.objects.create(
        vendor_id=vendor_id,
        date=datetime.now(),
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        average_response_time=average_response_time,
        fulfillment_rate=fulfillment_rate
    )



def compare_dates(actual_date, delivery_date):
    actual_date = datetime.strptime(actual_date, "%Y-%m-%d")
    delivery_date = datetime.strptime(delivery_date, "%Y-%m-%d")
    return actual_date <= delivery_date


def difference_dates(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    return (end_date - start_date).days
   
