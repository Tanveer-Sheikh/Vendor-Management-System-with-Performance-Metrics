from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('vendors/', views.createVendor),
     path('vendors/<int:vendor_id>/', views.createVendor,name='ViewVendor'),
     path('vendors/<int:vendor_id>/performance/', views.perfomance),
     path('purchase_orders/', views.purchaseOrder,name='OrderPurchase'),
     path('purchase_orders/<int:po_number>/acknowledge/', views.acknowledge_po),
     path('purchase_orders/<int:po_number>/', views.purchaseOrder,name='ViewOrders'),
]