from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User


class TestView(APIView):
    def get(self, request):
        return Response({'message': 'Test successful'})


class RegisterView(APIView):
    def post(self, request):
        return Response({'message': 'Register successful'})


class LoginView(APIView):
    def post(self, request):
        username=request.data.get('username')
        password=request.data.get('password')
        try:
            user=User.objects.get(username=username)
            if user.password==password:
                return Response({'message': 'Login successful'})
            else:
                return Response({'message': 'Invalid password'},status=401)
        except User.DoesNotExist:
            return Response({'message': 'User not found'},status=404)


class LogoutView(APIView):
    def post(self, request):
        return Response({'message': 'Logout successful'})


class ProfileView(APIView):
    def get(self, request,username):
        try:
            user=User.objects.get(username=username)
            return Response({'name': user.name,'email':user.email,'storage_used':user.storage_used,'storage_limit':user.storage_limit,'tenent':user.tenent,'password':user.password})
        except User.DoesNotExist:
            return Response({'message': 'User not found'},status=404)