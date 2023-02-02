import datetime

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import generics
from rest_framework.response import Response

from todo_list.models import TodoList
from todo_list.serializers import TodoListCreateSerializer, TodoListRetrieveSerializer
from todo_list.services import get_data_response


class TodoListCreateAPIView(generics.CreateAPIView):
    serializer_class = TodoListCreateSerializer


class TodoListRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TodoListRetrieveSerializer

    @extend_schema(parameters=[
        OpenApiParameter(name='uuid', description='uuid', required=True)
    ])
    def get(self, request, *args, **kwargs):
        model_uuid = request.query_params.get('uuid')
        data = get_data_response(self.serializer_class, TodoList.objects.filter(uuid=model_uuid))
        return data


class TodoListGetAPIView(generics.ListAPIView):
    serializer_class = TodoListRetrieveSerializer
    queryset = TodoList.objects.all()


class TodoListGetDatedAPIView(generics.ListAPIView):
    serializer_class = TodoListRetrieveSerializer

    @extend_schema(parameters=[
        OpenApiParameter(name='start', description='start_date', required=True,
                         type=datetime.date),
        OpenApiParameter(name='end', description='end_date', required=True,
                         type=datetime.date),
    ])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        start_date_str = self.request.query_params.get('start')
        start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')

        end_date_str = self.request.query_params.get('end')
        end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')

        queryset = TodoList.objects.filter(created__gte=start_date, created__lte=end_date)

        return queryset


class TodoListDeleteAPIView(generics.DestroyAPIView):
    serializer_class = TodoListRetrieveSerializer
    queryset = TodoList.objects.all()

    @extend_schema(parameters=[
        OpenApiParameter(name='uuid', description='uuid', required=True)
    ])
    def delete(self, request, *args, **kwargs):
        model_uuid = request.query_params.get('uuid')
        TodoList.objects.filter(uuid=model_uuid).delete()

        return Response(status=204)
