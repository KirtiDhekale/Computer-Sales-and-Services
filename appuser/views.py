from django.shortcuts import render, redirect
from appuser.models import Admin, Customer, Enquiry, Ticket
from appadmin.models import Product
from datetime import datetime


def index(request):
    return render(request, 'appuser/index.html')


def products(request):
    try:
        productss = Product.objects.all()
        return render(request, 'appuser/products.html', {'productss': productss})
    except Exception as ex:
        return render(request, 'appuser/products.html', {'message': ex})


def about(request):
    try:
        return render(request, 'appuser/about.html')
    except Exception as ex:
        return render(request, 'appuser/about.html', {'message': ex})


def enquiry(request):
    if request.method == 'POST':
        try:
            eid = datetime.now().strftime('%d%m%y%I%M%S')
            enquiry = Enquiry()
            enquiry.eid = eid
            enquiry.smobile = str(request.POST.get('smobile')).strip()
            enquiry.sname = str(request.POST.get('sname')).strip()
            enquiry.smessage = str(request.POST.get('smessage')).strip()
            enquiry.save(force_insert=True)
            message = 'Message has been sent successfully'
        except Exception as ex:
            message = ex
        return render(request, 'appuser/enquiry.html', {'message': message})
    else:
        return render(request, 'appuser/enquiry.html')


def registration(request):
    if request.method == 'POST':
        try:
            customer = Customer()
            customer.cmobile = str(request.POST.get('cmobile')).strip()
            customer.cpassword = str(request.POST.get('cpassword')).strip()
            customer.cname = str(request.POST.get('cname')).strip()
            customer.caddress = str(request.POST.get('caddress')).strip()
            customer.save(force_insert=True)
            message = 'Registration done successfully.'
        except Exception as ex:
            message = ex
        return render(request, 'appuser/registration.html', {'message': message})
    else:
        return render(request, 'appuser/registration.html')


def login(request):
    if request.method == 'POST':
        try:
            urole = str(request.POST.get('urole')).strip()
            if urole == "admin":
                admin = Admin.objects.get(amobile=request.POST.get('umobile'))
                if admin.apassword == str(request.POST.get('upassword')).strip():
                    request.session['uname'] = "Admin"
                    return redirect('appadmin/viewenquiries')
            else:
                customer = Customer.objects.get(cmobile=request.POST.get('umobile'))
                if customer.cpassword == str(request.POST.get('upassword')).strip():
                    request.session['cname'] = customer.cname
                    request.session['cmobile'] = customer.cmobile
                    request.session['caddress'] = customer.caddress
                    return redirect('customer/generateticket')
            message = 'Login failed'
        except Exception as ex:
            message = ex
        return render(request, 'appuser/login.html', {'message': message})
    else:
        return render(request, 'appuser/login.html')


def generateticket(request):
    try:
        message = ''
        products = Product.objects.all()
        if request.method == 'POST':
            ticket = Ticket()
            ticket.tid = datetime.now().strftime('%d%m%y%I%M%S')
            ticket.tdate = datetime.now().strftime('%d %b %Y')
            ticket.pname = str(request.POST.get('pname')).strip()
            ticket.cname = str(request.session["cname"]).strip()
            ticket.cmobile = str(request.session["cmobile"]).strip()
            ticket.caddress = str(request.session["caddress"]).strip()
            ticket.cmessage = str(request.POST.get('cmessage')).strip()
            ticket.tstatus = "Pending"
            ticket.save(force_insert=True)
            message = 'Ticket generated successfully.'
    except Exception as ex:
        return render(request, 'customer/generateticket.html', {'message': ex})
    return render(request, 'customer/generateticket.html', {'message': message, 'products': products})


def viewticket(request):
    try:
        tickets = Ticket.objects.filter(cmobile=str(request.session["cmobile"]).strip())
        return render(request, 'customer/viewticket.html', {'tickets': tickets})
    except Exception as ex:
        return render(request, 'appadmin/viewticket.html', {'message': ex})
