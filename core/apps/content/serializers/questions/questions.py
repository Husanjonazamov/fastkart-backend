from rest_framework import serializers

from ...models import QuestionsModel


class BaseQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListQuestionsSerializer(BaseQuestionsSerializer):
    class Meta(BaseQuestionsSerializer.Meta): ...


class RetrieveQuestionsSerializer(BaseQuestionsSerializer):
    class Meta(BaseQuestionsSerializer.Meta): ...


class CreateQuestionsSerializer(BaseQuestionsSerializer):
    class Meta(BaseQuestionsSerializer.Meta): ...
