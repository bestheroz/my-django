from django.db import transaction
from rest_framework import serializers

from mydjango.codes.models import CodeGroup, Code


class CodeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeGroup
        fields = "__all__"

    @transaction.atomic
    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user.username
        validated_data["updated_by"] = self.context["request"].user.username
        return super().create(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        validated_data["updated_by"] = self.context["request"].user.username
        return super().update(instance, validated_data)


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = "__all__"

    @transaction.atomic
    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user.username
        validated_data["updated_by"] = self.context["request"].user.username
        return super().create(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        validated_data["updated_by"] = self.context["request"].user.username
        return super().update(instance, validated_data)
