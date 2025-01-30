from rest_framework import serializers
from django.db import transaction
from ...models import StoreModel, ReviewModel
from core.apps.content.serializers.image import ListImageSerializer
from core.apps.accounts.serializers.user import UserSerializer
from core.apps.address.serializers.country import ListCountrySerializer
from core.apps.address.serializers.state import ListStateSerializer
from core.apps.product.serializers.review import ListReviewSerializer
from core.apps.content.models import ImageModel
from core.apps.accounts.models.user import User
from core.apps.address.models import StateModel, CountryModel


class BaseStoreSerializer(serializers.ModelSerializer):
    store_logo = ListImageSerializer(read_only=True)
    store_cover = ListImageSerializer(read_only=True)
    vendor = UserSerializer(read_only=True)
    country = ListCountrySerializer(read_only=True)
    state = ListStateSerializer(read_only=True)
    reviews = ListReviewSerializer(many=True)
    order_amount = serializers.FloatField()
    created_by_id = serializers.CharField()

    class Meta:
        model = StoreModel
        fields = [
            "id",
            "name",
            "description",
            "slug",
            "city",
            "address",
            "pincode",
            "facebook",
            "twitter",
            "instagram",
            "youtube",
            "pinterest",
            "hide_vendor_email",
            "hide_vendor_phone",
            "created_by_id",
            "status",
            "is_approved",
            "created_at", 
            "updated_at",
            "deleted_at",
            "orders_count",
            "reviews_count",
            "products_count",
            "order_amount",
            "rating_count",
            "store_logo",
            "store_cover",
            "vendor",
            "country",
            "state",
            'reviews'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['hide_vendor_email'] = 1 if instance.hide_vendor_email else 0
        data['hide_vendor_phone'] = 1 if instance.hide_vendor_phone else 0
        data['status'] = 1 if instance.status else 0
        data['is_approved'] = 1 if instance.is_approved else 0
        return data


class ListStoreSerializer(BaseStoreSerializer):
    class Meta(BaseStoreSerializer.Meta):
        pass


class RetrieveStoreSerializer(BaseStoreSerializer):
    class Meta(BaseStoreSerializer.Meta):
        pass


class CreateStoreSerializer(serializers.ModelSerializer):
    class Meta(BaseStoreSerializer.Meta): ...
    
    # created_by_id = serializers.IntegerField()
    # store_logo = serializers.IntegerField(required=False)
    # store_cover = serializers.IntegerField(required=False)
    # vendor = serializers.IntegerField(required=False)
    # country = serializers.IntegerField(required=False)
    # state = serializers.IntegerField(required=False)
    # hide_vendor_email = serializers.IntegerField(required=False)
    # hide_vendor_phone = serializers.IntegerField(required=False)
    # status = serializers.IntegerField(required=False)
    # is_approved = serializers.IntegerField(required=False)
    # reviews = serializers.PrimaryKeyRelatedField(queryset=ReviewModel.objects.all(), many=True, required=False)

    # class Meta:
    #     model = StoreModel
    #     fields = [
    #         "id",
    #         "name",
    #         "description",
    #         "slug",
    #         "city",
    #         "address",
    #         "pincode",
    #         "facebook",
    #         "twitter",
    #         "instagram",
    #         "youtube",
    #         "pinterest",
    #         "hide_vendor_email",
    #         "hide_vendor_phone",
    #         "created_by_id",
    #         "status",
    #         "is_approved",
    #         "created_at", 
    #         "updated_at",
    #         "deleted_at",
    #         "orders_count",
    #         "reviews_count",
    #         "products_count",
    #         "order_amount",
    #         "rating_count",
    #         "store_logo",
    #         "store_cover",
    #         "vendor",
    #         "country",
    #         "state",
    #         'reviews'
    #     ]

    # def create(self, validated_data):
    #     store_logo_id = validated_data.pop("store_logo", None)
    #     store_cover_id = validated_data.pop("store_cover", None)
    #     vendor_id = validated_data.pop("vendor", None)
    #     country_id = validated_data.pop("country", None)
    #     state_id = validated_data.pop("state", None)
    #     created_by_id = validated_data.pop("created_by_id", None)
    #     hide_vendor_email = validated_data.pop("hide_vendor_email", None)
    #     hide_vendor_phone = validated_data.pop("hide_vendor_phone", None)
    #     status = validated_data.pop("status", None)
    #     is_approved = validated_data.pop("is_approved", None)

    #     with transaction.atomic():
    #         store = StoreModel.objects.create(**validated_data)

    #         if store_logo_id:
    #             store.store_logo = ImageModel.objects.get(id=store_logo_id)
    #         if store_cover_id:
    #             store.store_cover = ImageModel.objects.get(id=store_cover_id)
    #         if vendor_id:
    #             store.vendor = User.objects.get(id=vendor_id)
    #         if country_id:
    #             store.country = CountryModel.objects.get(id=country_id)
    #         if state_id:
    #             store.state = StateModel.objects.get(id=state_id)
    #         if created_by_id:
    #             store.created_by = User.objects.get(id=created_by_id)

    #         if hide_vendor_email is not None:
    #             store.hide_vendor_email = bool(hide_vendor_email)
    #         if hide_vendor_phone is not None:
    #             store.hide_vendor_phone = bool(hide_vendor_phone)
    #         if status is not None:
    #             store.status = bool(status)
    #         if is_approved is not None:
    #             store.is_approved = bool(is_approved)

    #         store.save()

    #     return store
