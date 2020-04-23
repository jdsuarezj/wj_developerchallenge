from django.urls import path
from .views import login_view, register_user

urlpatterns = [
    # Login path
    path('login/', login_view, name="login"),
    # Signup path
    path('signup/', register_user, name="signup")    
]
