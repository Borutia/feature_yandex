from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.utils.http import urlsafe_base64_decode

from .models import Email, Report
from . import serializers


def get_email_instance(user_id):
    try:
        return Email.objects.get(user_id=user_id)
    except Email.DoesNotExist:
        raise NotFound(detail='Instance not found')


class EmailView(APIView):

    def get(self, request, user_id):
        """API GET /email/$user_id"""
        instance = get_email_instance(user_id)
        serializer = serializers.EmailGetSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """API POST /email"""
        serializer = serializers.EmailPostSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(
                {
                    'user_id': data['user_id'],
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, user_id):
        """API PATCH /email"""
        instance = get_email_instance(user_id)
        serializer = serializers.EmailUpdateSerializer(
            instance,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'user_id': instance.user_id,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        """API DELETE /email"""
        instance = get_email_instance(user_id)
        instance.email = None
        instance.is_confirmed = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmailConfirmView(APIView):

    def get(self, request):
        """API GET email/confirm"""
        email = request.GET.get('email', '')
        confirmation_code = request.GET.get('confirmation_code', '')
        user_id = urlsafe_base64_decode(confirmation_code).decode()
        instance = get_email_instance(user_id)
        if instance.email == email:
            instance.is_confirmed = True
            instance.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ReportView(APIView):

    def post(self, request):
        """API POST /report"""
        pass
