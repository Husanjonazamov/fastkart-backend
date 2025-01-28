from rest_framework import serializers

from ...models import ReviewModel
from core.apps.accounts.serializers.user import UserSerializer
from core.apps.product.models.product import ProductModel
from core.apps.accounts.models.user import User
from core.apps.content.models import ImageModel




class BaseReviewSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(required=False)
    consumer_id = serializers.IntegerField(required=False)
    store_id = serializers.IntegerField(source="store.id", read_only=True)
    review_image_id = serializers.IntegerField(required=False)
    consumer = UserSerializer(read_only=True)
    
    
    class Meta:
        model = ReviewModel
        fields = [
            "id",
            "product_id",
            "consumer_id",
            "store_id",
            "review_image_id",
            "rating",
            "description",
            "created_at",
            "updated_at",
            "deleted_at",
            "review_image",
            "consumer",
        ]
        read_only_fields = [
            "id",
            "store_id",
            "created_at",
            "updated_at",
            "deleted_at",
        ]

        def save(self, **kwargs):
            product_id = self.validated_data.get("product_id")
            consumer_id = self.validated_data.get("consumer_id")
            review_image_id = self.validated_data.get("review_image_id")
            rating = self.validated_data.get("rating")
            description = self.validated_data.get("description")
            review = ReviewModel.objects.create(
                product=ProductModel.objects.get(id=product_id),
                consumer=User.objects.get(id=consumer_id),
                rating=rating,
                description=description,
            )
            if review_image_id:
                review.review_image_id = review_image_id
                review.save()
            return review


class ListReviewSerializer(BaseReviewSerializer):
    class Meta(BaseReviewSerializer.Meta): ...


class RetrieveReviewSerializer(BaseReviewSerializer):
    class Meta(BaseReviewSerializer.Meta): ...


class CreateReviewSerializer(BaseReviewSerializer):
    class Meta(BaseReviewSerializer.Meta):
        pass

    def create(self, validated_data):
        product_id = validated_data.get("product_id")
        consumer_id = validated_data.get("consumer_id")
        review_image_id = validated_data.get("review_image_id")
        rating = validated_data.get("rating")
        description = validated_data.get("description")

        try:
            product = ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            raise serializers.ValidationError({"product_id": "Product not found."})

        try:
            consumer = User.objects.get(id=consumer_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"consumer_id": "Consumer not found."})

        review = ReviewModel.objects.create(
            product=product,
            consumer=consumer,
            rating=rating,
            description=description
        )

        if review_image_id:
            try:
                review_image = ImageModel.objects.get(id=review_image_id)
                review.review_image = review_image
                review.save()
            except ImageModel.DoesNotExist:
                raise serializers.ValidationError({"review_image_id": "Review image not found."})

        return review


