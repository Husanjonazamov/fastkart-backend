from rest_framework import serializers

from ...models import ReviewModel


class BaseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListReviewSerializer(BaseReviewSerializer):
    class Meta(BaseReviewSerializer.Meta): ...


class RetrieveReviewSerializer(BaseReviewSerializer):
    class Meta(BaseReviewSerializer.Meta): ...


class CreateReviewSerializer(BaseReviewSerializer):
    class Meta(BaseReviewSerializer.Meta): ...
