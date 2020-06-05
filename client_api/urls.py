from django.urls import path
from . import views

urlpatterns = [
    path('upload-invoice/', views.UploadInvoiceAPIView.as_view()),
    path('invoice-status/<slug:invoice_no>', views.InvoiceStatus.as_view()),
    path('invoice/<slug:invoice_no>', views.InvoiceDetail.as_view()),
    # path('invoice/', views.InvoiceAPIView.as_view()),
]
