from .views import SnackListView, SnackDetailView
from django.urls import path


urlpatterns = [
    path("",SnackListView.as_view(),name="snacks"),
    path("<int:pk>/",SnackDetailView.as_view(),name="snack_detail"),
]