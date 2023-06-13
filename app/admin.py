from django.contrib import admin
from app.models import Item, Purchaser, PurchaseRequisition, Employee, Manager, FinanceOfficer, Vendor, Quotation, Quo_Item, PR_Item, PO_Item,PurchaseOrder

admin.site.register(Purchaser)
admin.site.register(PurchaseRequisition)
admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(FinanceOfficer)
admin.site.register(Vendor)
admin.site.register(Quotation)
admin.site.register(Quo_Item)
admin.site.register(PurchaseOrder)
admin.site.register(PR_Item)
admin.site.register(PO_Item)
