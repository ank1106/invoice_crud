from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    SerializerMethodField,
    FileField,
    ValidationError
)
from .models import Invoice, InvoiceItem
from .utils import mockInvoiceParser

class InvoiceItemSerializer(ModelSerializer):
    
    class Meta:
        model = InvoiceItem
        exclude = ('invoice',)
        read_only_fields = ('invoice', 'id',)

class InvoiceSerializer(ModelSerializer):
    items = SerializerMethodField()
    customer = SerializerMethodField()

    class Meta:
        model = Invoice
        exclude = ('raw_invoice',)
        read_only_fields = ('invoice_no', 'id', 'customer',)

    def get_items(self, invoice):
        items = InvoiceItem.objects.filter(invoice=invoice)
        return InvoiceItemSerializer(items, many=True).data

    def get_customer(self, invoice):
        return invoice.customer.username

    def validateItems(self, items):
        for item in items:
            ser = InvoiceItemSerializer(data=item)
            if not ser.is_valid():
                return ser.error
        return None


    def updateItems(self, items, invoice):
        InvoiceItem.objects.filter(invoice=invoice).delete()
        for item in items:
            ser = InvoiceItemSerializer(data=item)
            if ser.is_valid():
                obj = ser.save()
                obj.invoice = invoice
                obj.save()

        return True


class InvoiceStatusSerializer(ModelSerializer):
    
    class Meta:
        model = Invoice
        fields = ('is_digitized', 'invoice_no')

    
class InvoiceUploadSerializer(Serializer):
    file = FileField()

    def __init__(self, *args, **kwargs):
        if kwargs.get('user'):
            self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def validate(self, data):
        """
            check for pdf extension and file size
        """
        ext = data["file"].name.split('.')[-1]
        if ext != "pdf":
            raise ValidationError("Only pdf files are allowed")
        if data["file"].size > 1000000: # !MB
            raise ValidationError("File size should not exceed 1 MB")
        self.file = data["file"]
        return True

    def save(self):
        return mockInvoiceParser(self.file, self.user)


