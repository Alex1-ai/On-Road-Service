from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from .models import CustomerService
from .models import CarEngineers
from django.core.mail import EmailMessage
from django.conf import settings

User = get_user_model()
# Create your views here.


def home(request):

    return render(request, 'index.html')


def service(request):
    if request.user.is_authenticated:
        customer = request.user.first_name

        messages.info(request, f"Welcome {customer}, To our services")
        return render(request, 'service.html')

    else:
        messages.warning(
            request, "Please Login before you can access this page!!")
        return render(request, 'login.html')


def createAccount(request):
    if request.method == 'POST':
        print('i am in the firstname container')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # to check if the email already exist
            if User.objects.filter(email=email).exists():
                messages.warning(
                    request, ' Email already Used, Please Use another Email !!')
                return redirect(createAccount)
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, mobile=mobile, email=email, password=password)
                user.save()
                print(first_name, last_name, mobile,
                      email, password, password2)
                messages.info(
                    request, f"{first_name} Your account has been created successfully")
                return redirect('login')

        else:
            messages.warning(
                request, " Password and repeat Password are not the same, Try Again !")
            return redirect('createAccount')

    else:
        return render(request, 'createAccount.html')

    # return render(request, 'createAccount.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # print(email, password)
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('service')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'Thanks for using our Service!!!')
    return redirect('/')


def contact(request):
    return render(request, 'contact.html')


def serviceForm(request):
    if request.method == 'POST':
        carName = request.POST['carName']
        phoneNumber = request.POST['phoneNumber']
        location = request.POST['location']
        address = request.POST['address']
        message = request.POST['message']
        # print(carName, phoneNumber, location, address, message)
        currentCustomer = request.user
        customer = currentCustomer.first_name
        customerEmail = currentCustomer.email
        print(customerEmail)

        # customerService = CustomerService.objects.create(
        #     carName=carName, phoneNumber=phoneNumber, location=location, address=address, message=message, customerService=currentCustomer)
        # customerService.save()
        # engineerLocation = CarEngineers.objects.values('garage_location')
        # locationE = engineerLocation
        # i = CarEngineers.objects.filter(
        #     garage_location=location).values('email')

        #EngineersEmail = i[0]['email']

        EngineersInformation = CarEngineers.objects.filter(
            garage_location=location).values().all()

        EngineersEmail = EngineersInformation[0]['email']
        EngineersNumber = EngineersInformation[0]['phone_number']
        EngineersName = EngineersInformation[0]['first_name']

        customer = request.user.first_name
        # print(EngineersInformation)
        print(EngineersEmail, EngineersName, EngineersNumber)

        # messageForAdmin = f"Name: {contactName} \n emial : {contactEmail} \n message: {contactMessage}"
        # adminEmail = 'alexanderemmanuel1719@gmail.com'
        # print(carName, phoneNumber, location, address, message)
        contactSubject = 'On Road Service'
        messageForCompany = f"Customer : {customer} \n Customer number:{phoneNumber} \n Car Name: {carName} \n  Location : {location} \n Address: {address} \n Customer Feedback : {message}"
        adminEmail = 'alexanderemmanuel1719@gmail.com'
        # for admins working in the company
        email_message_company_admin = EmailMessage(
            contactSubject,
            messageForCompany,
            settings.EMAIL_HOST_USER,
            [adminEmail],
        )
        email_message_company_admin.send()

        # engineers working in the company
        email_message_company = EmailMessage(
            contactSubject,
            messageForCompany,
            settings.EMAIL_HOST_USER,
            [EngineersEmail],
        )
        email_message_company.send()

        messageForCustomer = f"Thanks {customer} ,\n We received your call for our service. \nwe have sent our engineer to you. \n Engineer Name: {EngineersName} \n Engineer contact: {EngineersNumber}"

        email_message = EmailMessage(
            contactSubject,
            messageForCustomer,
            settings.EMAIL_HOST_USER,
            [customerEmail],
        )
        email_message.send()
        # print(locationE)
        messages.info(
            request, f"{customer} We got your request, Thanks we are coming to render our quality service!. for enquiry call: 0238559158")
        return render(request, 'index.html')
        # else:
        #     messages.warning(
        #         request, "Please try again!, Something went wrong")
    elif request.user.is_authenticated:
        return render(request, 'serviceform.html')

    else:
        messages.warning(request, 'pleasse Login to get access this page!')
        return render(request, 'login.html')
