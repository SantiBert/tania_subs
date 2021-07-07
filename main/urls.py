from django.urls import path
from .views import LendingCreateView

urlpatterns = [
    path('', LendingCreateView, name='inicio'),
]
