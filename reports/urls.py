from django.urls import path

from .views import EmailView, ReportView

urlpatterns = [
    path('email/<int:user_id>', EmailView.as_view(), name='email'),
    path('email', EmailView.as_view(), name='email_create'),
    path('report', ReportView.as_view(), name='report'),
]
