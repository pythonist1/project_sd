from django.urls import path

from .views import deals, DealView

urlpatterns = [
    path('deals/<str:pk>/', DealView.as_view()),
    path('deals/', deals),
]