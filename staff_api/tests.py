from django.test import TestCase
from client_api.models import Invoice, InvoiceItem
from django.contrib.auth.models import User
from django.test import Client


class InvoiceTestCase(TestCase):
    def setUp(self):
        self.request = Client()
        self.staff = User.objects.create_user('test_staff', 'teststaff@gmail.com', 'test_staff')
        self.staff.is_staff = True
        self.staff.save()
        self.request.login(username='test_staff', password='test_staff')

    
    def test_update_invoice_by_staff(self):
        # upload file
        with open('samples/invoice-sample.pdf', 'rb') as f:
            response = self.request.post('/client/upload-invoice/', 
                {'file':f})
            if response.status_code == 201:
                invoice_no = response.json()["invoice_no"]
            self.assertEqual(response.status_code , 201)

        # update total_price
        response = self.request.put(f'/staff/invoice-update/{invoice_no}', {"total_price":400, "is_digitized":True}, content_type="application/json")
        self.assertEqual(response.status_code , 200)

        # check if updated
        response = self.request.get(f'/staff/invoice/{invoice_no}')
        self.assertEqual(response.json()["total_price"] , "400.00")
        self.assertEqual(response.json()["is_digitized"] , True)
        
