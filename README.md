Certainly! Here's a structured and detailed README for your project:

---

# Vendor and Purchase Order Management System

## Overview

This project provides an API for managing vendors and purchase orders. It allows users to create, retrieve, update, and delete vendors and purchase orders. The system also tracks and calculates various performance metrics for vendors, such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
  - [Vendor APIs](#vendor-apis)
    - [Create a Vendor](#create-a-vendor)
    - [Retrieve All Vendors](#retrieve-all-vendors)
    - [Retrieve a Specific Vendor](#retrieve-a-specific-vendor)
    - [Update a Vendor](#update-a-vendor)
    - [Delete a Vendor](#delete-a-vendor)
  - [Purchase Order APIs](#purchase-order-apis)
    - [Create a Purchase Order](#create-a-purchase-order)
    - [Retrieve All Purchase Orders](#retrieve-all-purchase-orders)
    - [Acknowledge a Purchase Order](#acknowledge-a-purchase-order)
    - [Update a Purchase Order](#update-a-purchase-order)
    - [Delete a Purchase Order](#delete-a-purchase-order)
- [Performance Metrics](#performance-metrics)

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Download Source Code From GitHub :
   ```bash
   git clone https://github.com/Tanveer-Sheikh/vendor-purchase-order-management.git
   cd vendor-purchase-order-management
   ```
2. Download Django Rest:
   ```bash
   pip install Django-rest
   ```
3. Path:
   open Folder of manage.py in shell
4. Run the migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Vendor APIs

#### Create a Vendor

- **URL**: `/api/vendors/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "name": "Tanveer Sheikh",
      "contact_details": "123-456-7890",
      "address": "123 Vendor St.",
      "vendor_code": "VN123",
      "on_time_delivery_rate": 0,
      "quality_rating_avg": 0,
      "average_response_time": 0,
      "fulfillment_rate": 0
  }
  ```
- **Response**:
  ```json
  {
      "message": "Vendor created successfully"
  }
  ```

#### Retrieve All Vendors

- **URL**: `/api/vendors/`
- **Method**: `GET`
- **Response**:
  ```json
  {
      "data": {
          "28": {
              "name": "Tanveer Sheikh",
              "contact_details": "123-456-7890",
              "address": "123 Vendor St.",
              "vendor_code": "VN123",
              "on_time_delivery_rate": 0.0,
              "quality_rating_avg": 0.0,
              "average_response_time": 0.0,
              "fulfillment_rate": 0.0
          }
      }
  }
  ```

#### Retrieve a Specific Vendor

- **URL**: `/api/vendors/{vendor_id}/`
- **Method**: `GET`
- **Response**:
  ```json
  {
      "data": {
          "id": 28,
          "name": "Tanveer Sheikh",
          "contact_details": "123-456-7890",
          "address": "123 Vendor St.",
          "vendor_code": "VN123",
          "on_time_delivery_rate": 0.0,
          "quality_rating_avg": 0.0,
          "average_response_time": 0.0,
          "fulfillment_rate": 0.0
      }
  }
  ```

#### Update a Vendor

- **URL**: `/api/vendors/{vendor_id}/`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
      "name": "Tanveer Sheikh",
      "contact_details": "123-456-7890",
      "address": "123 Vendor St.",
      "vendor_code": "VN123",
      "on_time_delivery_rate": 1.0,
      "quality_rating_avg": 5.0,
      "average_response_time": 0.0,
      "fulfillment_rate": 1.0
  }
  ```
- **Response**:
  ```json
  {
      "message": "Vendor updated successfully"
  }
  ```

#### Delete a Vendor

- **URL**: `/api/vendors/{vendor_id}/`
- **Method**: `DELETE`
- **Response**:
  ```json
  {
      "message": "Vendor deleted successfully"
  }
  ```

### Purchase Order APIs

#### Create a Purchase Order

- **URL**: `/api/purchase_orders/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "po_number": "101",
      "vendor_id": 28,
      "order_date": "2024-06-01",
      "delivery_date": "2024-06-10",
      "items": "Item description",
      "quantity": 100,
      "status": "pending",
      "quality_rating": 5,
      "issue_date": null,
      "acknowledgment_date": null
  }
  ```
- **Response**:
  ```json
  {
      "message": "Purchase order created successfully"
  }
  ```

#### Retrieve All Purchase Orders

- **URL**: `/api/purchase_orders/`
- **Method**: `GET`
- **Response**:
  ```json
  {
      "101": {
          "po_number": "101",
          "vendor_id": 28,
          "order_date": "2024-06-01",
          "delivery_date": "2024-06-10",
          "items": "Item description",
          "quantity": 100,
          "status": "pending",
          "quality_rating": 5.0,
          "issue_date": null,
          "acknowledgment_date": null
      }
  }
  ```

#### Acknowledge a Purchase Order

- **URL**: `/api/purchase_orders/{po_number}/acknowledge/`
- **Method**: `POST`
- **Response**:
  ```json
  {
      "data": "Acknowledged"
  }
  ```

#### Update a Purchase Order

- **URL**: `/api/purchase_orders/{po_number}/`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
      "po_number": "101",
      "vendor_id": 28,
      "order_date": "2024-06-01",
      "delivery_date": "2024-06-10",
      "items": "Item description",
      "quantity": 100,
      "status": "completed",
      "quality_rating": 5.0,
      "issue_date": "2024-06-12",
      "acknowledgment_date": "2024-06-12"
  }
  ```
- **Response**:
  ```json
  {
      "message": "Purchase order updated successfully"
  }
  ```

#### Delete a Purchase Order

- **URL**: `/api/purchase_orders/{po_number}/`
- **Method**: `DELETE`
- **Response**:
  ```json
  {
      "message": "Purchase order deleted successfully"
  }
  ```
#### Specific Vendor Detail
- **URL**: `vendors/<int:vendor_id>/performance/`
- **Method**: `GET`
- **Response**:
  ```json
{
    "data": {
        "id": 28,
        "name": "Tanveer Sheikh",
        "contact_details": "123-456-7890",
        "address": "123 Vendor St.",
        "vendor_code": "VN123",
        "on_time_delivery_rate": 1.0,
        "quality_rating_avg": 5.0,
        "average_response_time": 0.0,
        "fulfillment_rate": 1.0
    }
}
  ```



## Performance Metrics

The performance metrics for vendors are tracked and updated based on the purchase orders. The metrics include:
- **On-time Delivery Rate**: Percentage of orders delivered on or before the delivery date.
- **Quality Rating Average**: Average quality rating given to the vendor.
- **Average Response Time**: Average time taken by the vendor to acknowledge the purchase orders.
- **Fulfillment Rate**: Percentage of orders fulfilled by the vendor.

Feel free to customize this README as needed to better fit your project and preferences. This structured format should provide clear and comprehensive documentation for users of your API.
