from django.shortcuts import render, redirect
from .models import Member
from django.core.mail import send_mail
from django.http import JsonResponse
import requests

from django.core.exceptions import ValidationError
from .validator import validate_nullable_integer
from .validator import parse_and_validate_date
def index(request):
    return render(request, 'index.html')

def submit_membership(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        voter_id = request.POST.get("voter_id")
        membership_id = request.POST.get("membership_id")
        citizenship_number = request.POST.get("citizenship_number")
        perm_wardno = request.POST.get("perm_wardno")
        current_wardno = request.POST.get("current_wardno")
        family_count = request.POST.get("family_count")
        worktenure1 = request.POST.get("worktenure1")
        worktenure2 = request.POST.get("worktenure2")
        worktenure3 = request.POST.get("worktenure3")
        worktenure4 = request.POST.get("worktenure4")
        worktenure5 = request.POST.get("worktenure5")
        # year_joined = request.POST.get("year_joined")

        birth_date = request.POST.get("birth_date")
        membership_date = request.POST.get("membership_date")
        print(birth_date)
        print(membership_date)

        integer_fields = {
            "phone": phone,
            "citizenship_number": citizenship_number,
            "membership_id": membership_id,
            "voter_id": voter_id,
            "perm_wardno": perm_wardno,
            "current_wardno": current_wardno,
            "family_count": family_count,
            "worktenure1": worktenure1,
            "worktenure2": worktenure2,
            "worktenure3": worktenure3,
            "worktenure4": worktenure4,
            "worktenure5": worktenure5,
            # "year_joined": year_joined,
        }
        validated_fields = {}
        try:
            for field_name, field_value in integer_fields.items():
                validated_value = validate_nullable_integer(field_value)
                validated_fields[field_name] = validated_value
        except ValidationError as e:
            error_message = str(e)
            return render(request, 'fail.html', {'error_message': error_message})
        
        try:
            validated_birth_date = parse_and_validate_date(birth_date)
            validated_membership_date = parse_and_validate_date(membership_date)
        except ValidationError as e:
            print("Date validation error:", str(e))
            error_message = str(e)
            return render(request, 'datefail.html', {'error_message': error_message})
        
        photo = request.POST.get("photo")
        name = request.POST.get("name")
        
        membership_type = request.POST.get("membership_type")
        membership_duration = request.POST.get("membership_duration")

        email = request.POST.get("email")
        perm_province = request.POST.get("perm_province")
        perm_district = request.POST.get("perm_district")
        perm_constituency = request.POST.get("perm_constituency")
        perm_constituencyB = request.POST.get("perm_constituencyB")
        perm_palika = request.POST.get("perm_palika")
        perm_voting_center = request.POST.get("perm_voting_center")
        current_province = request.POST.get("current_province")
        current_district = request.POST.get("current_district")
        current_constituency = request.POST.get("current_constituency")
        current_constituencyB = request.POST.get("current_constituencyB")
        current_palika = request.POST.get("current_palika")
        current_voting_center = request.POST.get("current_voting_center")
        father_mother_name = request.POST.get("father_mother_name")
        husband_or_wife_name = request.POST.get("husband_or_wife_name")
        education = request.POST.get("education")
        religion = request.POST.get("religion")
        caste = request.POST.get("caste")
        
        marital_status = request.POST.get("marital_status")
        past_responsibility = request.POST.get("past_responsibility")
        company1 = request.POST.get("company1")
        jobtitle1 = request.POST.get("jobtitle1")
        company2 = request.POST.get("company2")
        jobtitle2 = request.POST.get("jobtitle2")
        company3 = request.POST.get("company3")
        jobtitle3 = request.POST.get("jobtitle3")
        company4 = request.POST.get("company4")
        jobtitle4 = request.POST.get("jobtitle4")
        company5 = request.POST.get("company5")
        jobtitle5 = request.POST.get("jobtitle5")
        name_of_approver = request.POST.get("name_of_approver")
        position_of_approver = request.POST.get("position_of_approver")

        new_member = Member(
            photo=photo,
            name=name,
            birth_date=validated_birth_date,
            # birth_date=birth_date,

            membership_type=membership_type,
            membership_duration=membership_duration,

            citizenship_number=validated_fields["citizenship_number"],
            voter_id=validated_fields["voter_id"],
            phone=validated_fields["phone"],
            email=email,
            perm_province=perm_province,
            perm_district=perm_district,
            perm_constituency=perm_constituency,
            perm_constituencyB=perm_constituencyB,
            perm_palika=perm_palika,
            perm_wardno=validated_fields["perm_wardno"],
            perm_voting_center=perm_voting_center,
            current_province=current_province,
            current_district=current_district,
            current_constituency=current_constituency,
            current_constituencyB=current_constituencyB,
            current_palika=current_palika,
            current_wardno=validated_fields["current_wardno"],
            current_voting_center=current_voting_center,
            father_mother_name=father_mother_name,
            husband_or_wife_name=husband_or_wife_name,
            family_count=validated_fields["family_count"],
            education=education,
            religion=religion,
            marital_status=marital_status,
            caste=caste,
            # year_joined=validated_fields["year_joined"],

            membership_date=validated_membership_date,
            # membership_date=membership_date,

            membership_id=validated_fields["membership_id"],
            past_responsibility=past_responsibility,
            company1=company1,
            jobtitle1=jobtitle1,
            worktenure1=validated_fields["worktenure1"],
            company2=company2,
            jobtitle2=jobtitle2,
            worktenure2=validated_fields["worktenure2"],
            company3=company3,
            jobtitle3=jobtitle3,
            worktenure3=validated_fields["worktenure3"],
            company4=company4,
            jobtitle4=jobtitle4,
            worktenure4=validated_fields["worktenure4"],
            company5=company5,
            jobtitle5=jobtitle5,
            worktenure5=validated_fields["worktenure5"],
            name_of_approver=name_of_approver,
            position_of_approver=position_of_approver,
        )

        new_member.save()

        email = request.POST.get('email')
        if email:
            subject = 'Membership Submission'
            message = f'Thank you for submitting your email: {email}'
            sender_email = 'utshabbardewa2055@gmail.com'  # Replace with your sender email
            recipient_list = [email]
            send_mail(subject, message, sender_email, recipient_list)

        return redirect("payment")
    return render(request, 'payment.html')

def payment_page(request):
    return render(request, "payment.html")

def id_card(request):
    # Logic for generating the ID card goes here
    # You can pass any necessary data to the template
    return render(request, "id_card.html")

# Khalti 
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
