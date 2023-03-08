from django.urls import path
from .views import CustomTokenObtainPairView, HelloWorldView,UserRegistrationView

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user_registration'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/hello/', HelloWorldView.as_view(), name='hello_world'),

    ]

