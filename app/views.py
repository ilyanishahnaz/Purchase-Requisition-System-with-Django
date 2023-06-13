from django.shortcuts import render, redirect
import random
# Create your views here.
from django.http import HttpRequest

from django.template import RequestContext
from datetime import datetime

from django.contrib.auth.decorators import login_required
from app.models import PurchaseRequisition
from app.models import Quotation
from app.models import PR_Item, Employee
from app.models import Quo_Item, PO_Item, PurchaseOrder
from app.models import FinanceOfficer
from django.db.models import Sum
from app.forms import QuotationForm, QuoItemForm
from .prform import PRForm, PR_Item_Form

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
            }
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Dr. Yeoh.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'ABC System',
            'message':'This application processes ...',
            'year':datetime.now().year,
        }
    )

@login_required
def menu(request):
    check_employee = request.user.groups.filter(name='employee').exists()
    check_manager = request.user.groups.filter(name='Manager').exists()
    check_fo = request.user.groups.filter(name='FinanceOfficer').exists()
    check_pr = request.user.groups.filter(name='Purchaser').exists()
    manager_name = request.user.first_name
    PR = PurchaseRequisition.objects.all()
    PR_count = PR.count()
    Quo = Quotation.objects.all()
    Quo_count = Quo.count()

    context = {
            'title':'Main Menu',
            'is_employee': check_employee,
            'is_manager': check_manager,
            'is_fo': check_fo,
            'is_pr': check_pr,
            'year':datetime.now().year,
            'PR_count' : PR_count,
            'Quo_count' : Quo_count,
            'manager_name': manager_name,
            
        }
    context['user'] = request.user

    return render(request,'app/menu.html',context)

def searchPR(request):
    if request.method == "POST":
        searched = request.POST['searched']
        formID = PurchaseRequisition.objects.filter(formID__contains=searched)
        return render(
            request,
            'app/approvePR/searchPR.html',
            {
                'searched': searched,
                'formID' : formID,
            }
        )
    else:
        return render(request, 
        'app/searchPR.html',{})

def searchSelectedPR(request):
    if request.method == "POST":
        searched = request.POST['searched']
        formID = PurchaseRequisition.objects.filter(formID__contains=searched)
        return render(
            request,
            'app/viewPR/searchSelectedPR.html',
            {
                'searched': searched,
                'formID' : formID,
            }
        )
    else:
        return render(request, 
        'app/viewPR/searchSelectedPR.html',{})

def searchQuoSelect(request):
    if request.method == "POST":
        searched = request.POST['searched']
        formID = PurchaseRequisition.objects.filter(formID__contains=searched)
        return render(
            request,
            'app/selectQuo/searchQuoSelect.html',
            {
                'searched': searched,
                'formID' : formID,
            }
        )
    else:
        return render(request, 
        'app/selectQuo/searchQuoSelect.html',{})

def searchPRQuo(request):
    if request.method == "POST":
        searched = request.POST['searched']
        formID = PurchaseRequisition.objects.filter(formID__contains=searched)
        return render(
            request,
            'app/viewAppQuo/searchPRQuo.html',
            {
                'searched': searched,
                'formID' : formID,
            }
        )
    else:
        return render(request, 
        'app/viewAppQuo/searchPRQuo.html',{})

def viewPRItem(request):
    if request.method == "POST":
        formID = request.POST['formID']
        purchase_requisition = PurchaseRequisition.objects.filter(formID=formID)
        pr_items = PR_Item.objects.filter(formID=formID)
        total_price = pr_items.aggregate(Sum('totalPrice'))
        total_price_sum = total_price['totalPrice__sum']
        
        return render(
            request,
            'app/approvePR/viewPRItem.html',
            {
                'formID' : formID,
                'pr' : purchase_requisition,
                'pr_items' : pr_items,
                'total_price_sum': total_price_sum,
            }
        )
    else:
        return render(request,'app/approvePR/viewPRItem.html',{})

def viewSelectedPR(request):
    if request.method == "POST":
        formID = request.POST['formID']
        purchase_requisition = PurchaseRequisition.objects.filter(formID=formID)
        pr_items = PR_Item.objects.filter(formID=formID)
        total_price = pr_items.aggregate(Sum('totalPrice'))
        total_price_sum = total_price['totalPrice__sum']
        return render(
            request,
            'app/viewPR/viewSelectedPR.html',
            {
                'formID' : formID,
                'pr' : purchase_requisition,
                'pr_items' : pr_items,
                'total_price_sum': total_price_sum,
            }
        )
    else:
        return render(request,'app/viewPR/viewSelectedPR.html',{})

def viewPRQuo(request):
    if request.method == "POST":
        formID = request.POST['formID']
        purchase_requisition = PurchaseRequisition.objects.filter(formID=formID)
        quotation = Quotation.objects.filter(formID=formID)
        return render(
            request,
            'app/selectQuo/viewPRQuo.html',
            {
                'formID' : formID,
                'pr' : purchase_requisition,
                'quotation' : quotation,
            }
        )
    else:
        return render(request,'app/selectQuo/viewPRQuo.html',{})


def viewApprovedQuo(request):
    if request.method == "POST":
        formID = request.POST['formID']
        purchase_requisition = PurchaseRequisition.objects.filter(formID=formID)
        quotation = Quotation.objects.filter(formID=formID)
        return render(
            request,
            'app/viewAppQuo/viewApprovedQuo.html',
            {
                'formID' : formID,
                'pr' : purchase_requisition,
                'quotation' : quotation,
            }
        )
    else:
        return render(request,'app/viewAppQuo/viewApprovedQuo.html',{})


def uploadedQuo(request):
    if request.method == "POST":
        quoID = request.POST['quoID']
        quotation = Quotation.objects.filter(quoID=quoID)
        quo_items = Quo_Item.objects.filter(quoID=quoID)
        vendor = quotation.first().vendID
        total_price = quo_items.aggregate(Sum('totalPrice'))
        total_price_sum = total_price['totalPrice__sum']
        return render(
            request,
            'app/selectQuo/uploadedQuo.html',
            {
                'quoID' : quoID,
                'quotation' : quotation,
                'quo_items' : quo_items,
                'total_price_sum': total_price_sum,
                'vendor' : vendor,
            }
        )
    else:
        return render(request,'app/selectQuo/uploadedQuo.html',{})


def viewAppQuo(request):
    if request.method == "POST":
        quoID = request.POST['quoID']
        quotation = Quotation.objects.filter(quoID=quoID)
        quo_items = Quo_Item.objects.filter(quoID=quoID)
        vendor = quotation.first().vendID
        total_price = quo_items.aggregate(Sum('totalPrice'))
        total_price_sum = total_price['totalPrice__sum']
        return render(
            request,
            'app/viewAppQuo/viewAppQuo.html',
            {
                'quoID' : quoID,
                'quotation' : quotation,
                'quo_items' : quo_items,
                'total_price_sum': total_price_sum,
                'vendor' : vendor,
            }
        )
    else:
        return render(request,'app/viewAppQuo/viewAppQuo.html',{})

def status_quo(request):
    if request.method == "POST":
        quoID = request.POST.get('quoID')
        StatusQuo = request.POST.get('StatusQuo')
        Quotation.objects.filter(quoID=quoID).update(StatusQuo=StatusQuo)
        quotation = Quotation.objects.filter(quoID=quoID)
        quo_items = Quo_Item.objects.filter(quoID=quoID)
        return render(
            request,
            'app/selectQuo/quoConfirmation.html',
            {
                'quoID' : quoID,
                'quotation' : quotation,
                'quo_items' : quo_items,
            }
        )
    else:
        return render(request,'app/selectQuo/uploadedQuo.html',{})


def update_status(request):
    if request.method == "POST":
        formID = request.POST.get('formID')
        formStatus = request.POST.get('formStatus')
        PurchaseRequisition.objects.filter(formID=formID).update(formStatus=formStatus)
        purchase_requisition = PurchaseRequisition.objects.filter(formID=formID)
        pr_items = PR_Item.objects.filter(formID=formID)
        return render(
            request,
            'app/approvePR/statusconfirmation.html',
            {
                'formID' : formID,
                'pr' : purchase_requisition,
                'pr_items' : pr_items,
            }
        )
    else:
        return render(request,'app/approvePR/viewPRItem.html',{})



def searchQuo2(request):
    if request.method == "POST":
        searched = request.POST['searched']
        ID = Quotation.objects.filter(quoID__contains=searched)
        return render(
            request,
            'app/selectQuo/searchQuo2.html',
            {
                'searched': searched,
                'ID' : ID,
            }
        )
    else:
        return render(request, 
        'app/selectQuo/searchQuo2.html',{})

def approvePR(request):
    """Renders the approvePR page."""
    PR_list = PurchaseRequisition.objects.all()
    return render(
        request,
        'app/approvePR/approvePR.html',
        {
            'title':'Approve Purchase Requisition',
            'year':datetime.now().year,
            'PR_list' : PR_list,
        }
    )

def approveQuo(request):
    Quo_list = Quotation.objects.all()
    PR_list = PurchaseRequisition.objects.all()
    return render(
        request,
        'app/selectQuo/approveQuo.html',
        {
            'title':'Select Quotation',
            'year':datetime.now().year,
            'Quo_list' : Quo_list,
            'PR_list' : PR_list,
        }
    )

def viewQuo(request):
    Quo_list = Quotation.objects.all()
    PR_list = PurchaseRequisition.objects.all()
    return render(
        request,
        'app/viewAppQuo/viewQuo.html',
        {
            'title':'View Selected Quotation',
            'year':datetime.now().year,
            'Quo_list' : Quo_list,
            'PR_list' : PR_list,
        }
    )

def viewPR(request):
    PR_list = PurchaseRequisition.objects.all()
    return render(
        request,
        'app/viewPR/viewPR.html',
        {
            'title':'View Approved Purchase Requisition',
            'year':datetime.now().year,
            'PR_list' : PR_list,
        }
    )

def createQuo(request):
    if request.method == "POST":
        quoForm = QuotationForm(request.POST)
        if quoForm.is_valid():
            quoForm.save()
            return redirect('addQuoItem')
    else :
        quoForm = QuotationForm

    return render(
        request,
        'app/createQuo.html',
        {
            'title':'Create Quotation',
            'year':datetime.now().year,
            'quoForm' : quoForm,
        }
    )

def addQuoItem(request):
    if request.method == "POST":
        if "add_item" in request.POST:
            itemForm = QuoItemForm()
            return render(request, 'app/addQuoItem.html', {'itemForm': itemForm})
        else:
            itemForm = QuoItemForm(request.POST)
            if itemForm.is_valid():
                itemForm.save()
                # redirect to a page that lists all the items added so far
                return redirect('addQuoItem')
    else:
        itemForm = QuoItemForm()
    return render(request, 'app/addQuoItem.html', {'itemForm': itemForm})


def confirm(request):
    return render(request,'app/confirm.html',{})

def generatepo(request):
    Quo_list = Quotation.objects.all()
    return render(
        request,
        'app/GeneratePO/generatepo.html',
        {
            'title': 'Generate Purchase Order',
            'year': datetime.now().year,
            'Quo_list': Quo_list,
        }
    )


def generatepoform(request):
    if request.method == "POST":
        quoID = request.POST['quoID']
        orderID = random.randint(100000, 999999)
        request.session['orderID'] = orderID
        fo_name = request.user.first_name
        quotation = Quotation.objects.filter(quoID=quoID)
        quo_items = Quo_Item.objects.filter(quoID=quoID)
        shipDate = datetime.now().strftime("%b. %d, %Y")
        vendor = quotation.first().vendID
        total_price = quo_items.aggregate(Sum('totalPrice'))
        total_price_sum = total_price['totalPrice__sum']
        return render(
            request,
            'app/GeneratePO/generatepoform.html',
            {
                'quoID': quoID,
                'quotation': quotation,
                'quo_items': quo_items,
                'total_price_sum': total_price_sum,
                'vendor': vendor,
                'fo_name': fo_name,
                'shipDate': shipDate,
                'orderID': orderID,

            }
        )
    else:
        return render(request,'app/GeneratePO/generatepoform.html')


def create_po(request):
    if request.method == "POST":
            quoID = request.POST.get('quoID')
            vendor = Quotation.objects.get(quoID=quoID).vendID
            managerID = Quotation.objects.get(quoID=quoID).managerID
            delAddress = Quotation.objects.get(quoID=quoID).delAddress
            shipDate = datetime.now().strftime("%Y-%m-%d")
            quotation = Quotation.objects.filter(quoID=quoID)
            quo_items = Quo_Item.objects.filter(quoID=quoID)
            foID = FinanceOfficer.objects.get(financeID=request.user.username)
            orderID = request.session.get('orderID')
            purchase_order = PurchaseOrder.objects.create(orderID=orderID, vendorID=vendor, foID=foID, managerID=managerID, delAddress=delAddress)
            for quo_item in quo_items:
                PO_Item.objects.create(itemID=quo_item.itemID,orderID=purchase_order,itemName=quo_item.itemName,quantity=quo_item.quantity,unitPrice=quo_item.unitPrice,totalPrice=quo_item.totalPrice,shipDate=shipDate)
            return render(
            request,
            'app/GeneratePO/poconfirmation.html',
            {
            'quoID' : quoID,
            'vendor' : vendor,
            'managerID' : managerID,
            'delAddress' : delAddress,
            'quotation' : quotation,
            'quo_items' : quo_items,
            'orderID': orderID,
            
            }
                )
    else:
        return render(request,'app/GeneratePO/generatepoform.html',{})
    
def viewpo(request):
    PO_list = PurchaseOrder.objects.all()
    Quo_list = Quotation.objects.all()
    po_items = PO_Item.objects.all()
    quo_items = Quo_Item.objects.all()
    return render(
        request,
        'app/ViewPO/viewpo.html',
        {
            'title': 'View Purchase Order',
            'year': datetime.now().year,
            'PO_list': PO_list,
            'po_items': po_items,
            'quo_items': quo_items,
        }
    )


def viewselectedpo(request):
    if request.method == "POST":
        orderID = request.POST['orderID']
        fo_name = request.user.first_name
        shipDate = PO_Item.objects.filter(orderID=orderID).first().shipDate
        purchaseorder = PurchaseOrder.objects.filter(orderID=orderID)
        po_items = PO_Item.objects.filter(orderID=orderID)
        vendorID = PurchaseOrder.objects.filter(orderID=orderID).first().vendorID
        total_price = po_items.aggregate(Sum('totalPrice'))
        total_price_sum = total_price['totalPrice__sum']
        return render(
            request,
            'app/ViewPO/viewselectedpo.html',
            {
                'orderID': orderID,
                'purchaseorder': purchaseorder,
                'po_items': po_items,
                'total_price_sum': total_price_sum,
                'vendorID': vendorID,
                'fo_name': fo_name,
                'shipDate': shipDate,

            }
        )
    else:
        return render(request, 'app/ViewPO/viewpo.html', {})

# Employee

from .prform import PRForm, PR_Item_Form

def viewPRbyemp(request):
    # PR_list = PurchaseRequisition.objects.filter(empID=request.user.id)
    employee = Employee.objects.get(user=request.user)
    PR_list = PurchaseRequisition.objects.all().filter(empID=employee)
    return render(
        request,
        'app/viewPRbyemp/viewPRbyemp.html',
        {
            'title':'View Purchase Requisition Created',
            'year':datetime.now().year,
            'PR_list' : PR_list,
        }
    )

def createPR(request):
    if request.method == "POST":
        prForm = PRForm(request.POST)
        if prForm.is_valid():
            prForm.save()
            return redirect('addPRItem')
    else :
        prForm = PRForm

    return render(
        request,
        'app/createPR.html',
        {
            'title':'Create Purchase Requisition',
            'year':datetime.now().year,
            'prForm' : prForm,
        }
    )

def addPRItem(request):
    if request.method == "POST":
        if "add_item" in request.POST:
            itemForm = PR_Item_Form()
            return render(request, 'app/addPRItem.html', {'itemForm': itemForm})
        else:
            itemForm = PR_Item_Form(request.POST)
            if itemForm.is_valid():
                itemForm.save()
                # redirect to a page that lists all the items added so far
                return redirect('addPRItem')
    else:
        itemForm = PR_Item_Form()
    return render(request, 'app/addPRItem.html', {'itemForm': itemForm})




# def getPRItem(request):




