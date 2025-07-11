from django.urls import path
from .views import LogAPIView

urlpatterns = [
    path('logs/', LogAPIView.as_view(), name='logs'),
]
