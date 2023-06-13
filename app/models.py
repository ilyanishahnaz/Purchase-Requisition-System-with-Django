"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User
from datetime import date
#sharing entity

#class PR_Item(models.Model):

class Employee(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    empID = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=30)
    F_Name = models.TextField(max_length=30)
    L_Name = models.TextField(max_length=30)
    email = models.CharField(max_length=30)
    department = models.TextField(max_length=30)
    def __str__(self):
        return "%s %s" % (self.F_Name, self.L_Name)

class Manager(models.Model):
    managerID = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=30)
    F_Name = models.TextField(max_length=30)
    L_Name = models.TextField(max_length=30)
    email = models.CharField(max_length=30)
    department = models.TextField(max_length=30)
    def __str__(self):
        return "%s %s" % (self.F_Name, self.L_Name)

class Purchaser(models.Model):
    purchaserID = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=30)
    F_Name = models.TextField(max_length=30)
    L_Name = models.TextField(max_length=30)
    email = models.CharField(max_length=30)
    department = models.TextField(max_length=30)
    def __str__(self):
        return "%s %s" % (self.F_Name, self.L_Name)

class FinanceOfficer(models.Model):
    financeID = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=30)
    F_Name = models.TextField(max_length=30)
    L_Name = models.TextField(max_length=30)
    email = models.CharField(max_length=30)
    department = models.TextField(max_length=30)
    def __str__(self):
        return "%s %s" % (self.F_Name, self.L_Name)

class Vendor(models.Model):
    vendorID = models.CharField(primary_key=True, max_length=10)
    vendorName = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    zipCode = models.IntegerField()
    State = models.TextField(max_length=30)
    contactNum = models.CharField(max_length=15)
    def __str__(self):
        return str(self.vendorID)
    
class PurchaseRequisition(models.Model):
    formID = models.CharField(primary_key=True, max_length=10)
    empID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    managerID = models.ForeignKey(Manager, on_delete=models.CASCADE)
    formDate = models.DateField(default=date.today)
    requiredBy = models.DateField(default=date.today)
    delAddress = models.CharField(max_length=50)
    def __str__(self):
        return str(self.formID)    
    class Status(models.TextChoices):
        APPROVED = "Approved"
        REJECTED = "Rejected"
        PENDING = "Pending"

    formStatus = models.TextField(
        choices = Status.choices,
        default = Status.PENDING
    )

class Quotation(models.Model):
    quoID = models.CharField(primary_key=True, max_length=10)
    vendID = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=None, related_name='quotation')
    formID = models.ForeignKey(PurchaseRequisition, on_delete=models.CASCADE, default=None)
    purchaserID = models.ForeignKey(Purchaser, on_delete=models.CASCADE)
    managerID = models.ForeignKey(Manager, on_delete=models.CASCADE)
    quoDate = models.DateField(default=date.today)
    delAddress = models.CharField(max_length=50)
    def __str__(self):
        return str(self.quoID)    
    class StatusQuo(models.TextChoices):
        APPROVED = "Approved"
        REJECTED = "Rejected"
        PENDING = "Pending"

    StatusQuo = models.TextField(
        choices = StatusQuo.choices,
        default = StatusQuo.PENDING
    )

class PurchaseOrder(models.Model):
    orderID = models.CharField(primary_key=True, max_length=10)
    vendorID = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=None)
    foID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    managerID = models.ForeignKey(Manager, on_delete=models.CASCADE)
    quoDate = models.DateField
    delAddress = models.CharField(max_length=50)
    def __str__(self):
        return str(self.quoID) 

class PR_Item(models.Model):
    itemID = models.CharField(primary_key=True, max_length=10)
    formID = models.ForeignKey(PurchaseRequisition, on_delete=models.CASCADE)
    itemName = models.TextField(max_length=30)
    quantity = models.IntegerField()
    unitPrice = models.FloatField()
    totalPrice = models.FloatField()
    def __str__(self):
        return str(self.itemID)

class Quo_Item(models.Model):
    itemID = models.CharField(primary_key=True, max_length=10)
    quoID = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    itemName = models.TextField(max_length=30)
    quantity = models.IntegerField()
    unitPrice = models.FloatField()
    totalPrice = models.FloatField()
    def __str__(self):
        return str(self.quoID)

class PO_Item(models.Model):
    itemID = models.CharField(primary_key=True, auto_created = True, max_length=10)
    orderID = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    itemName = models.TextField(null=True,default=None, blank=True)
    quantity = models.IntegerField()
    unitPrice = models.FloatField()
    totalPrice = models.FloatField()
    shipDate = models.DateField()
    def __str__(self):
        return str(self.itemID)

class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    item_name = models.TextField()
    item_description = models.TextField(null=True,default=None, blank=True)
    def __str__(self):
        return str(self.item_id)

