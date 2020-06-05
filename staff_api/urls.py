from django.urls import path
from . import views

urlpatterns = [
    path('invoice/<slug:invoice_no>', views.InvoiceDetail.as_view()),
    path('invoice-update/<slug:invoice_no>', views.InvoiceUpdate.as_view()),
    # path('invoice/', views.InvoiceAPIView.as_view()),
]
