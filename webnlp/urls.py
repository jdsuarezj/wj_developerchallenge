from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    # Connection with the other urls
    path('admin/', admin.site.urls),    
    path("", include("users.urls")),
    path("", include("app.urls"))  
]
