from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Email, Report
from . import serializers


class EmailView(APIView):
    @staticmethod
    def get_instance(user_id):
        try:
            return Email.objects.get(user_id=user_id)
        except Email.DoesNotExist:
            raise NotFound(detail='Instance not found')

    def get(self, request, user_id):
        """API GET /email/$user_id"""
        instance = self.get_instance(user_id)
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
        instance = self.get_instance(user_id)
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
        instance = self.get_instance(user_id)
        instance.email = None
        instance.is_confirmed = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReportView(APIView):
    def post(self):
        """API POST /report"""
        pass
