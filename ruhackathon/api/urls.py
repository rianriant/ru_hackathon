from django.urls import path
from .views import (
  IventListCreateView
)

urlpatterns = [
  path('ivents/', IventListCreateView.as_view()),
]