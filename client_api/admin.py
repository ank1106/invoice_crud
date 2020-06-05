from django.contrib import admin

# Register your models here.
from .models import (
    Invoice, 
    InvoiceItem, 
)

admin.site.register(InvoiceItem)
admin.site.register(Invoice)