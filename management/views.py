# Page Redirect , Request Page , Response Page
from itertools import product
import json
from math import prod
from django.shortcuts import render, HttpResponse, redirect
# Showing Message alert on Main Page
from django.contrib import messages
# Create account
from django.contrib.auth.models import User, auth
from pip import main
# import Tables
from .models import *
# Login account
from django.contrib.auth import authenticate, login, logout
# Change Password
from django.contrib.auth.forms import PasswordChangeForm
# Gmail Request Add
from django.core.mail import send_mail
# Import json
from django.http import JsonResponse
# For Search Query
from django.db.models import Q
# Store User Image
from django.core.files.storage import FileSystemStorage
# CSRF Token
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Paytm Gateway
# from PayTm import Checksum
# Date Time
from django.utils.timezone import datetime
from datetime import date
import uuid
from django.conf import settings


def index(request):
    return render(request, 'index.html')


def add_user(request):
    if request.method == "POST":
        block = request.POST.get('block')
        number = request.POST.get('number')
        u_type = request.POST['u_type']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        gender = request.POST['gender']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        status = request.POST['status']
        m = Member.objects.create(
            block=block,
            number=number,
            u_type=u_type,
            f_name=f_name,
            l_name=l_name,
            gender=gender,
            address=address,
            contact=contact,
            email=email,
            status=status,
        )
    return render(request, 'add_user.html')


def user_list(request):
    member = Member.objects.all()
    return render(request, 'user_list.html', context={'member': member})


def delete_member(request, id):
    m = Member.objects.filter(id=id)
    m.delete()
    return redirect('/user_list')


def add_maintenance(request):
    if request.method == "POST":
        block = request.POST['block']
        installment = request.POST['installment']
        penalty = request.POST['penalty']
        dop = request.POST['dop']
        p_status = request.POST['p_status']
        status = request.POST['status']
        m = Maintenance.objects.create(
            block=block,
            installment=installment,
            penalty=penalty,
            dop=dop,
            p_status=p_status,
            status=status
        )
        return redirect('/maintenance_list')
    return render(request, 'add_maintenance.html')


def maintenance_list(request):
    maintenance = Maintenance.objects.all()
    return render(request, 'maintenance_list.html', context={'maintenance': maintenance})


def edit_maintenance(request, id):
    if request.method == "POST":
        installment = request.POST['installment']
        penalty = request.POST['penalty']
        p_status = request.POST.get('p_status')
        status = request.POST.get('status')
        m = Maintenance.objects.filter(id=id).update(
            installment=installment, penalty=penalty, p_status=p_status, status=status)
        return redirect('/maintenance_list')
    m = Maintenance.objects.get(id=id)
    return render(request, 'edit_maintenance.html', context={'m': m})


def delete_maintenance(request, id):
    m = Maintenance.objects.filter(id=id)
    m.delete()
    return redirect('/maintenance_list')


def add_notice(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        n = Notice.objects.create(title=title, desc=desc)
    return render(request, 'add_notice.html')


def notice_list(request):
    n = Notice.objects.all()
    return render(request, 'notice_list.html', context={'n': n})


def gallery(request):
    if request.method == "POST":
        try:
            image = request.FILES['img']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)
        except:
            pass
        return redirect('/admin')
    return render(request, 'gallery.html')


def handle_login(request):
    if request.method == "POST":
        username = request.POST['usrname']
        password = request.POST['pswd']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin')
    return render(request, 'login.html')


def handle_logout(request):
    logout(request)
    return redirect('/admin')
