from django.urls import path
from .views import HelloWorld
from .views import SecureHelloView
from rest_framework.authtoken.views import obtain_auth_token
from django.http import JsonResponse
from . import views


def home(request):
    return JsonResponse({'status': 'API is running 🚀'})

urlpatterns = [
    path('', home),  # Now visiting / will return a friendly message
    path('api/hello/', views.HelloView.as_view()),
    path('secure-hello/', SecureHelloView.as_view()),
    path('api-token-auth/', obtain_auth_token), 
]


