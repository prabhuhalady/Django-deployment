from django.urls import path
from .views import HomeView, PhotoUploadView, PhotoListView, ToggleLikeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload_photo/', PhotoUploadView.as_view(), name='upload_photo'),
    path('view_photos/', PhotoListView.as_view(), name='view_photos'),
    path('toggle_like/<int:photo_id>/', ToggleLikeView.as_view(), name='toggle_like'),
]
