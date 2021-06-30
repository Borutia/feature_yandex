from rest_framework import serializers

from .models import Email, Report
from .utils import get_email_instance


class EmailGetSerializer(serializers.ModelSerializer):
    """Serializer for get email"""

    class Meta:
        model = Email
        fields = '__all__'


class EmailPostSerializer(serializers.ModelSerializer):
    """Serializer for create email"""

    def create(self, validated_data):
        Email.objects.create(**validated_data)
        return validated_data

    def validate_email(self, email):
        if email is None:
            raise serializers.ValidationError('Email is empty!')
        return email

    def validate(self, validated_data):
        return validated_data

    class Meta:
        model = Email
        fields = ('user_id', 'email',)


class EmailUpdateSerializer(serializers.ModelSerializer):
    """Serializer for update email"""

    def update(self, instance, validated_data):
        instance.email = validated_data['email']
        instance.is_confirmed = False
        self.instance.save()
        return self.instance

    def validate_email(self, email):
        if email is None:
            raise serializers.ValidationError('Email is empty!')
        return email

    class Meta:
        model = Email
        fields = ('email',)


class ReportPostSerializer(serializers.ModelSerializer):
    """Serializer for create report"""
    order_id = serializers.IntegerField(min_value=1, required=False)
    user_id = serializers.IntegerField(min_value=1)

    def create(self, validated_data):
        order_id = None
        if 'order_id' in validated_data:
            order_id = validated_data.pop('order_id')
        report = Report.objects.create(**validated_data)
        if order_id:
            report.order_set.create(order_id=order_id)
        report.save()
        return report

    def validate(self, validated_data):
        user_id = validated_data.pop('user_id')
        email = get_email_instance(user_id)
        if not email.is_confirmed:
            raise serializers.ValidationError('email is not confirmed')
        validated_data['email'] = email
        if 'order_id' in validated_data:
            if 'date_from' in validated_data or 'date_to' in validated_data:
                raise serializers.ValidationError('order_id with date')
        else:
            if 'date_from' not in validated_data:
                raise serializers.ValidationError('date_from is empty')
            if 'date_to' not in validated_data:
                raise serializers.ValidationError('date_to is empty')
        return validated_data

    def validate_user_id(self, user_id):
        if user_id is None:
            raise serializers.ValidationError('user_id is empty')
        return user_id

    class Meta:
        model = Report
        fields = ('date_from', 'date_to', 'order_id', 'user_id',)
