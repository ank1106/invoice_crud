from django.test import TestCase
from .models import Invoice, InvoiceItem
from django.contrib.auth.models import User
from django.test import Client


class InvoiceTestCase(TestCase):
    def setUp(self):
        self.client_request = Client()
        self.staff_request = Client()
        self.client = User.objects.create_user('test_client', 'testclient@gmail.com', 'test_client')
        self.staff = User.objects.create_user('test_staff', 'teststaff@gmail.com', 'test_staff')
        self.staff.is_staff = True
        self.staff.save()
        self.client_request.login(username='test_client', password='test_client')
        self.staff_request.login(username='test_staff', password='test_staff')


    def test_upload_invoice_by_client(self):
        # upload file
        with open('samples/invoice-sample.pdf', 'rb') as f:
            response = self.client_request.post('/client/upload-invoice/', 
                {'file':f})
            if response.status_code == 201:
                invoice_no = response.json()["invoice_no"]
            self.assertEqual(response.status_code , 201)

        # check the status of uploaded file
        response = self.client_request.get(f'/client/invoice-status/{invoice_no}')
        self.assertEqual(response.json() , {"is_digitized":False, "invoice_no":invoice_no})
        

        # Should not be able to get mock data as it is not digitized
        response = self.client_request.get(f'/client/invoice/{invoice_no}')
        self.assertEqual(response.status_code , 404)

        # digitize the invoice
        response = self.staff_request.put(f'/staff/invoice-update/{invoice_no}', {"is_digitized":True}, content_type="application/json")
        self.assertEqual(response.status_code , 200)

        # check again the invoice status
        response = self.client_request.get(f'/client/invoice-status/{invoice_no}')
        self.assertEqual(response.json() , {"is_digitized":True, "invoice_no":invoice_no})

        # now this should work
        response = self.client_request.get(f'/client/invoice/{invoice_no}')
        self.assertEqual(response.status_code , 200)

