from django.urls import path
from .views import HelloWorld
from .views import SecureHelloView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('hello/', HelloWorld.as_view()), 
    path('secure-hello/', SecureHelloView.as_view()),
    path('api-token-auth/', obtain_auth_token), 
]
