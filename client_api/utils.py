import random
import string
from .models import Invoice, InvoiceItem
import pdftotext

def random_str(num, prefix='', number=False, lower_case=False):
    if number:
        return prefix+''.join(random.choice(string.digits) for _ in range(num))
    elif lower_case:
        return prefix+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(num))
    else:
        return prefix+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num))


SELLERS = ["Amazon", "Google Services", "Microsoft", "Cisco"] 
BUYERS = ["Infoteck", "Techsquare", "Dot Technology"] 

def mockInvoiceParser(file, user):
    """
        Mock function to mimic the parsing process like that of OCR and ML
        1. creates a new invoice object
        2. randomly adds items to it
        3. returns the invoice
    """
    pdf = pdftotext.PDF(file)
    raw_text = ""
    for page in pdf:
      raw_text+=page
    
    invoice = Invoice.objects.create(customer=user, 
        raw_invoice=raw_text, 
        invoice_no=random_str(4,"INV-", True), 
        seller=random.choice(SELLERS),
        buyer=random.choice(BUYERS),
    )
    items = []
    invoice.net_price = 0
    mock_items = range(random.choice(range(1,6)))
    for _ in mock_items:
        item = InvoiceItem.objects.create(invoice=invoice, 
            name=random_str(3, "Item-", True),
            qty=random.choice(range(1,3)),
            price=random.choice(range(50,100))
        )
        items.append(item)
        invoice.net_price += item.qty*item.price

    invoice.tax = 0.18*invoice.net_price
    invoice.total_price = invoice.tax+invoice.net_price
    invoice.save()
    return invoice
    


