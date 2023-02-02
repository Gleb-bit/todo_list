from rest_framework import serializers

from todo_list.models import TodoList
from todo_list.services import GenerateUUID


class TodoListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'


class TodoListCreateSerializer(TodoListRetrieveSerializer):

    def create(self, validated_data):
        generator_uuid = GenerateUUID(True, 8)
        model_uuid = generator_uuid.create_uuid()
        validated_data['uuid'] = model_uuid

        return super().create(validated_data)
