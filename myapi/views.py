from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Public endpoint
class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})

# Authenticated-only endpoint
class SecureHelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}! This is a secure endpoint."})
