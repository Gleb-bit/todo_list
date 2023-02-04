from django.urls import path, include

from todo_list.views import TodoListCreateAPIView, TodoListRetrieveAPIView, TodoListGetAPIView, TodoListGetDatedAPIView, \
    TodoListDeleteAPIView

urlpatterns = [
    path('record/', include([
        path('create', TodoListCreateAPIView.as_view(), name='create'),
        path('get', TodoListRetrieveAPIView.as_view(), name='get'),
        path('delete', TodoListDeleteAPIView.as_view(), name='delete'),

    ])),
    path('records/', include([
        path('all', TodoListGetAPIView.as_view(), name='all'),
        path('list', TodoListGetDatedAPIView.as_view(), name='list'),

    ])),

]
