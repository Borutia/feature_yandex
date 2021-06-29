from django.urls import path

from .views import EmailView, ReportView, EmailConfirmView

urlpatterns = [
    path('email/<int:user_id>', EmailView.as_view(), name='email'),
    path('email', EmailView.as_view(), name='email_create'),
    path('email/confirm', EmailConfirmView.as_view(), name='email_confirm'),
    path('report', ReportView.as_view(), name='report'),
]
