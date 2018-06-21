from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from Mobile.forms import *
from Mobile.tokens import account_activation_token
from Mobile.utils import render_to_pdf  # created in step 4
from .models import *
import datetime



def homepage(request):
     return render(request, 'Mobile/help2.html')
    # return HttpResponse("hello kk")


def mobilehomepage(request):
    context = {
        'name': 'dd',
    }
    return render(request, 'Mobile/home.html', {'context': context})


"""
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)  # get all data from html using post req
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            # return redirect("Mobile:login.html")
            return HttpResponse("success")

           OR 
           
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponse("success")


    else:
        form = SignUpForm()

    return render(request, 'Mobile/signup.html', {'form': form})

"""


def login_view(request):
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Mobile:mobilehomepage')  # name should be used  mobilehomepage

    else:
        form = AuthenticationForm()

    return render(request, "Mobile/login.html", {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        # return  redirect('Mobile:homepage')
        return HttpResponse("logout success")
    else:
        return HttpResponse("logout by get method")


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('Mobile/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignUpForm()
    return render(request, 'Mobile/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def bills_view(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content') and request.POST.get('name'):
            post = Post()
            post.name = request.POST.get('name')
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')

            post.save()

            return HttpResponse("sucees done saving")

    else:
        return render(request, 'Mobile/bill.html')


def additem_view(request):
    return render(request, 'Mobile/additem.html')


def bill_generate_view(request):
    if request.method == 'POST':
        billdb = Bill_Database()
        print(request.POST.get('customer_name'))
        print(request.POST.get('bill_no'))
        print(request.POST.get('customer_address'))
        print(request.POST.get('itemname'))

        billdb.save()
        data = {
            'today': datetime.datetime.now() ,
            'amount': request.POST.get('itemname'),
            'customer_name': request.POST.get('customer_name'),
            'order_id': 1233434,
        }
        pdf = render_to_pdf('Mobile/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    else:
        return render(request, 'Mobile/bill.html')


def generatepdf_View(request, *args, **kwargs):
    data = {
        'today': "today",
        'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'order_id': 1233434,
    }
    pdf = render_to_pdf('Mobile/invoice.html', data)
    return HttpResponse(pdf, content_type='application/pdf')
