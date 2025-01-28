from rest_framework import serializers

from ...models import QuestionsModel
from core.apps.accounts.models.user import User
from core.apps.product.models.product import ProductModel


class BaseQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsModel
        fields = [
            "id",
            "question",
            "answer",
            "consumer_id",
            "product_id",
            "created_at",
            "updated_at",
            "deleted_at",
            "reaction",
            "total_likes",
            "total_dislikes",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at"
        ]


class ListQuestionsSerializer(BaseQuestionsSerializer):
    class Meta(BaseQuestionsSerializer.Meta): ...


class RetrieveQuestionsSerializer(BaseQuestionsSerializer):
    class Meta(BaseQuestionsSerializer.Meta): ...


from rest_framework.exceptions import NotFound

class CreateQuestionsSerializer(BaseQuestionsSerializer):
    consumer_id = serializers.IntegerField(write_only=True, required=False)
    product_id = serializers.IntegerField(write_only=True, required=False)

    class Meta(BaseQuestionsSerializer.Meta):
        fields = BaseQuestionsSerializer.Meta.fields + ['consumer_id', 'product_id']

    def create(self, validated_data):
        consumer_id = validated_data.pop('consumer_id', None)
        product_id = validated_data.pop('product_id', None)

        consumer = User.objects.get(id=consumer_id) if consumer_id else None

        try:
            product = ProductModel.objects.get(id=product_id) if product_id else None
        except ProductModel.DoesNotExist:
            raise NotFound(f"Product with ID {product_id} does not exist.")

        question = QuestionsModel.objects.create(
            question=validated_data['question'],
            answer=validated_data['answer'],
            consumer=consumer,
            product=product,
            reaction=validated_data.get('reaction', None),
            total_likes=validated_data.get('total_likes', 0),
            total_dislikes=validated_data.get('total_dislikes', 0),
            deleted_at=validated_data.get('deleted_at', None),
        )
        return question
