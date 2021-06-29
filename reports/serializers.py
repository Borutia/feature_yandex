from rest_framework import serializers

from .models import Email, Report


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
