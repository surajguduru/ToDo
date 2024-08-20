from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todos.views import TodoViewSet, TodoListByPriorityViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Updated line with correct 'actions' argument
    # path('api/todos/priority/', TodoListByPriorityViewSet.as_view({'get': 'list'}), name='todos-by-priority'),
]
