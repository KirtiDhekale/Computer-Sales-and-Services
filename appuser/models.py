from django.db import models


class Admin(models.Model):
    amobile = models.TextField(primary_key=True)
    apassword = models.TextField()

    class Meta:
        db_table = 'tblAdmin'


class Customer(models.Model):
    cmobile = models.TextField(primary_key=True)
    cpassword = models.TextField()
    cname = models.TextField()
    caddress = models.TextField()

    class Meta:
        db_table = 'tblCustomer'


class Enquiry(models.Model):
    eid = models.TextField(primary_key=True)
    sname = models.TextField()
    smobile = models.TextField()
    smessage = models.TextField()

    class Meta:
        db_table = 'tblEnquiry'


class Ticket(models.Model):
    tid = models.TextField(primary_key=True)
    tdate = models.TextField()
    pname = models.TextField()
    cname = models.TextField()
    cmobile = models.TextField()
    caddress = models.TextField()
    cmessage = models.TextField()
    tstatus = models.TextField()

    class Meta:
        db_table = 'tblTicket'
