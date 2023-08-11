from django.shortcuts import render, redirect
from .models import Member
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'index.html')

def submit_membership(request):
    if request.method == "POST":
        name = request.POST.get("name")
        birth_date = request.POST.get("birth_date")
        citizenship_number = request.POST.get("citizenship_number")

        new_member = Member(name=name, birth_date=birth_date, citizenship_number=citizenship_number)
        new_member.save()

        return redirect("payment")

    return render(request, 'index.html')

def payment_page(request):
    return render(request, "payment.html")

def initiate_khalti_payment(request):
    url = "https://a.khalti.com/api/v2/epayment/initiate/"
    headers = {
        "Authorization": "Key 0ee3e3a99d294a01b700cb5c15323723",
        "Content-Type": "application/json"
    }
    data = {
        "return_url": "http://localhost:8000/payment/success",
        "website_url": "http://localhost:8000/payment/",
        "amount": 100000,
        "purchase_order_id": "12345",
        "purchase_order_name": "Raprapa id card",
        "customer_info": {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "9800000000"
        }
    }

    response = requests.post(url, json=data, headers=headers)
    payment_data = response.json()

    return JsonResponse(payment_data)

def id_card(request):
    # Logic for generating the ID card goes here
    # You can pass any necessary data to the template
    
    return render(request, "id_card.html")