from django.urls import path, re_path
from app import views

urlpatterns = [
    re_path(r'^.*\.html', views.pages, name='pages'),
    # Scan view path
    path('scan/', views.scan_view, name="scan"),
    # Index view path
    path('', views.index, name='home'),
]
