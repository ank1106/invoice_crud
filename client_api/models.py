from django.db import models
from django.contrib.auth.models import User


class Invoice(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    seller = models.CharField(max_length=100, null=True, blank=True)
    buyer = models.CharField(max_length=100, null=True, blank=True)
    invoice_no = models.CharField(max_length=50, unique=True)
    
    # parsed text from pdf
    raw_invoice = models.TextField()
    
    tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    net_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    
    is_digitized = models.BooleanField(default=False)
    
    def __str__(self):
        return self.invoice_no


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.invoice.invoice_no} -> {self.name}"
