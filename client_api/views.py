from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.generics import UpdateAPIView, CreateAPIView, RetrieveAPIView

from .models import (
    Invoice, 
    InvoiceItem, 
)
from .serializers import (
    InvoiceSerializer,
    InvoiceItemSerializer,
    InvoiceUploadSerializer,
    InvoiceStatusSerializer,
)
from django.conf import settings
from rest_framework.permissions import AllowAny

class UploadInvoiceAPIView(APIView):
    
    serializer_class = InvoiceUploadSerializer
    
    def post(self, request):
        ser = InvoiceUploadSerializer(data=request.data, user=request.user)
        if ser.is_valid():
            invoice = ser.save()
            return JsonResponse({"status":"OK", "invoice_no":invoice.invoice_no}, status=201)
        return JsonResponse(ser.errors, safe=False, status=400)


class InvoiceStatus(RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceStatusSerializer
    lookup_field = "invoice_no"


class InvoiceDetail(RetrieveAPIView):
    queryset = Invoice.objects.filter(is_digitized=True)
    serializer_class = InvoiceSerializer
    lookup_field = "invoice_no"