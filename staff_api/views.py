from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.generics import UpdateAPIView, CreateAPIView, RetrieveAPIView

from client_api.models import (
    Invoice, 
    InvoiceItem, 
)
from client_api.serializers import (
    InvoiceSerializer,
    InvoiceItemSerializer,
)

from django.conf import settings
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsStaff


class InvoiceDetail(RetrieveAPIView):
    permission_classes = (IsAuthenticated, IsStaff,)
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    lookup_field = "invoice_no"


class InvoiceUpdate(UpdateAPIView):
    permission_classes = (IsAuthenticated, IsStaff,)
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    lookup_field = "invoice_no"
    

    def put(self, requset, invoice_no):
    	invoice = self.get_object()
    	ser = InvoiceSerializer(invoice, data=requset.data)
    	if ser.is_valid():
    		if requset.data.get('items'):
	    		errors = ser.validateItems(requset.data["items"])
	    		if errors:
	    			return JsonResponse(errors)
	    		else:
	    			ser.updateItems(requset.data["items"], invoice)
	    	ser.save()
	    	return JsonResponse({"status":"OK"}, status=200)
    	return JsonResponse(ser.errors, status=400)

