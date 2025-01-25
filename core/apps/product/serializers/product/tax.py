from rest_framework import serializers
from core.apps.product.models.tax import TaxModel



class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxModel
        fields = [
            "name",
            "rate",
            "status",
            "created_by",
            "created_at",
            "updated_at",
            "deleted_at",
        ]
        
        read_only_fields = [
            "created_by",
            "created_at",
            "updated_at",
            "deleted_at",
        ]

