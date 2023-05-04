from django.urls import path
from .views import SnackListView, SnackDeleteView, SnackCreateView, SnackUpdateView, SnackDetailView


urlpatterns = [
    path('', SnackListView.as_view(), name='list_view'),
    path('<int:pk>/', SnackDetailView.as_view(), name='detail_view'),
    path('new/', SnackCreateView.as_view(), name='create_view'),
    path('<int:pk>/edit', SnackUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete', SnackDeleteView.as_view(), name='delete_view'),
]