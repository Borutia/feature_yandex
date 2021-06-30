from rest_framework import serializers

from .models import Email, Report
from .utils import get_email_instance


class EmailGetSerializer(serializers.ModelSerializer):
    """Serializer for get email"""

    class Meta:
        model = Email
        fields = ('user_id', 'email', 'is_confirmed',)


class EmailPostSerializer(serializers.ModelSerializer):
    """Serializer for create email"""
    email = serializers.EmailField(required=True)

    class Meta:
        model = Email
        fields = ('user_id', 'email',)


class EmailUpdateSerializer(serializers.ModelSerializer):
    """Serializer for update email"""

    def update(self, instance, validated_data):
        instance.email = validated_data['email']
        instance.is_confirmed = False
        instance.save()
        return instance

    def validate(self, validated_data):
        if 'email' not in validated_data:
            raise serializers.ValidationError('Email is empty!')
        return validated_data

    class Meta:
        model = Email
        fields = ('email',)


class ReportPostSerializer(serializers.ModelSerializer):
    """Serializer for create report with order"""
    order_id = serializers.IntegerField(min_value=1, required=True)
    user_id = serializers.IntegerField(min_value=1, required=True)

    def create(self, validated_data):
        order_id = validated_data.pop('order_id')
        report = Report.objects.create(**validated_data)
        report.order_set.create(order_id=order_id)
        report.save()
        return report

    def validate(self, validated_data):
        user_id = validated_data.pop('user_id')
        email = get_email_instance(user_id)
        if not email.is_confirmed:
            raise serializers.ValidationError('email is not confirmed')
        validated_data['email'] = email
        return validated_data

    class Meta:
        model = Report
        fields = ('order_id', 'user_id',)


class ReportPeriodPostSerializer(serializers.ModelSerializer):
    """Serializer for create report with period"""
    user_id = serializers.IntegerField(min_value=1, required=True)
    date_from = serializers.DateField(required=True)
    date_to = serializers.DateField(required=True)

    def validate(self, validated_data):
        user_id = validated_data.pop('user_id')
        email = get_email_instance(user_id)
        if not email.is_confirmed:
            raise serializers.ValidationError('email is not confirmed')
        validated_data['email'] = email
        return validated_data

    class Meta:
        model = Report
        fields = ('date_from', 'date_to', 'user_id',)
