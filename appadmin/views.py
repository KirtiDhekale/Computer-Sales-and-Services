from django.shortcuts import render
from appadmin.models import Product
from appuser.models import Enquiry, Ticket


def addproduct(request):
    if request.method == 'POST':
        try:
            pname = str(request.POST.get('pname')).strip()
            pimage = 'media/product/' + pname + '.jpg'
            with open(pimage, 'wb')as fw:
                fw.write(request.FILES['pimage'].read())
            product = Product()
            product.pname = pname
            product.pdescription = str(request.POST.get('pdescription')).strip()
            product.save(force_insert=True)
            message = 'Product details added successfully'
        except Exception as ex:
            message = ex
        return render(request, 'appadmin/addproduct.html', {'message': message})
    else:
        return render(request, 'appadmin/addproduct.html')


def viewproduct(request):
    try:
        if request.method == 'POST':
            pname = request.POST.get('pname')
            product = Product.objects.get(pname=pname)
            product.delete()
        products = Product.objects.all()
        return render(request, 'appadmin/viewproduct.html', {'products': products})
    except Exception as ex:
        return render(request, 'appadmin/viewproduct.html', {'message': ex})


def viewenquiries(request):
    try:
        if request.method == 'POST':
            eid = request.POST.get('eid')
            enquiry = Enquiry.objects.get(eid=eid)
            enquiry.delete()
        messages = Enquiry.objects.all()
        return render(request, 'appadmin/viewenquiries.html', {'messages': messages})
    except Exception as ex:
        return render(request, 'appadmin/viewenquiries.html', {'msg': ex})


def viewticket(request):
    try:
        if request.method == 'POST':
            tid = request.POST.get('tid')
            ticket = Ticket.objects.get(tid=tid)
            ticket.delete()
        tickets = Ticket.objects.all()
        return render(request, 'appadmin/viewticket.html', {'tickets': tickets})
    except Exception as ex:
        return render(request, 'appadmin/viewticket.html', {'message': ex})


def updateticket(request, tid):
    try:
        message =''
        if request.method == 'POST':
            ticket = Ticket.objects.get(tid=tid)
            ticket.tstatus = request.POST.get('tstatus')
            ticket.save(force_update=True)
            message = 'Ticket status updated successfully'
        ticket = Ticket.objects.get(tid=tid)
        return render(request, 'appadmin/updateticket.html', {'ticket': ticket, "message": message})
    except Exception as ex:
        return render(request, 'appadmin/updateticket.html', {'message': ex})
