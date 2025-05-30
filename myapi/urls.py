from django.urls import path
from .views import HelloWorld
from .views import SecureHelloView
from rest_framework.authtoken.views import obtain_auth_token
from django.http import JsonResponse


def home(request):
    return JsonResponse({'status': 'API is running 🚀'})

urlpatterns = [
    path('', home),
    path('api/hello/', HelloWorld.as_view()),  # ✅ Fix here
    path('secure-hello/', SecureHelloView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]

