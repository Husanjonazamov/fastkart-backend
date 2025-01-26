from rest_framework import serializers

from ...models import QuestionsModel


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


class CreateQuestionsSerializer(BaseQuestionsSerializer):
    class Meta(BaseQuestionsSerializer.Meta): ...
