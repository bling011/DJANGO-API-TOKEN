from django.urls import path
from .views import HelloWorld, SecureHelloView
from rest_framework.authtoken.views import obtain_auth_token
from django.http import JsonResponse

def home(request):
    return JsonResponse({'status': 'API is running 🚀'})

urlpatterns = [
    path('', home),  # Root URL
    path('hello/', HelloWorld.as_view()),
    path('secure-hello/', SecureHelloView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]


