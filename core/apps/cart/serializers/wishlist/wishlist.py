from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ...models import WishlistModel
from .wishlistitem import ListWishlistItemSerializer
from core.apps.accounts.models import User


class BaseWishlistSerializer(serializers.ModelSerializer):
    items = ListWishlistItemSerializer(many=True, read_only=True)
    consumer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    class Meta:
        model = WishlistModel
        fields = [
            "id",
            "items",
            "consumer",
            "total",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "created_at",
            "updated_at"
        ]


class ListWishlistSerializer(BaseWishlistSerializer):
    class Meta(BaseWishlistSerializer.Meta): ...


class RetrieveWishlistSerializer(BaseWishlistSerializer):
    class Meta(BaseWishlistSerializer.Meta): ...


class CreateWishlistSerializer(BaseWishlistSerializer):
    consumer = serializers.CharField()  
    total = serializers.IntegerField(default=0) 

    class Meta:
        model = WishlistModel
        fields = [
            'consumer',
            'total',
            "created_at",
            "updated_at",
        ]  

    def create(self, validated_data):
        consumer_id = validated_data.get('consumer')
        total = validated_data.get('total', 0)

        if not consumer_id:
            raise ValidationError("Consumer ID is required.")

        try:
            consumer = User.objects.get(id=consumer_id)
        except User.DoesNotExist:
            raise ValidationError("Consumer with provided ID does not exist.")

        wishlist = WishlistModel.objects.create(
            consumer=consumer,
            total=total
        )

        return wishlist

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['consumer'] = instance.consumer.id 
        return representation
