from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.authentication_app.serializers.user_serializer import auth_serializer, login_serializer
from apps.authentication_app.models.user_model import CustomUser
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import permissions
from apps.authentication_app.jwt_processor.jwt_generator import generate_jwt_token, generate_refresh_token
from apps.authentication_app.jwt_processor.jwt_decoder import decode_jwt_token
from pathlib import os
from dotenv import load_dotenv
load_dotenv()

JWT_SECRET=os.getenv('JWT_SECRET')

class Registration(APIView):
    """ Register a new user. """
    permission_classes=[permissions.AllowAny]

    def post(self, request):
        user_serializer=auth_serializer(data=request.data)

        if not user_serializer.is_valid():
            return Response({'errors': 'Error while registration please provide 8 digit password and unique email, phone '}, status=400)

        password = user_serializer.validated_data['password']
        user_serializer.validated_data['password'] = make_password(password) 
        user_serializer.save()
        return Response({'ok':'user registered' }, status=status.HTTP_201_CREATED)
        
class Login(APIView):
    """Function to login user"""
    permission_classes=[permissions.AllowAny]

    def post(self, request):
        signin_serializer= login_serializer(data=request.data)
        
        if signin_serializer.is_valid(): 
            email = signin_serializer.validated_data.get('email')
            password = signin_serializer.validated_data.get('password')
        
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response({'error': 'Invalid username'}, status=400)
            
            if check_password(password, user.password):
                if not user.is_active:
                    return Response({"error":"please activate account"}, status=401)
             
                #generate access main token
                jwt_token = generate_jwt_token(user.id, JWT_SECRET)

                # Generate refresh token
                refresh_token = generate_refresh_token(user.id, JWT_SECRET)    

                response=Response({
                    'token': jwt_token,
                    'refresh_token': refresh_token,
                    "ok":"cookies stored!",
                    },status=200)
                    
            
                # Set token in cookies
                response.set_cookie('access_token', jwt_token, httponly=True)
                response.set_cookie('refresh_token', refresh_token, httponly=True)

                return response

            else:
                return Response({"error":"invalid password!"}, status=400)

        else:
            return Response(signin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

class RefreshTokenView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return Response({"error": "Refresh token not found"}, status=401)

        try:
            payload = decode_jwt_token(refresh_token)
            user_id = payload['user_id']
            user = CustomUser.objects.get(id=user_id)

            # Check if the user is active
            if not user.is_active:
                return Response({"error": "User account is not active"}, status=401)

            # Generate a new access token
            new_access_token = generate_jwt_token(user.id, JWT_SECRET)

            return Response({"access_token": new_access_token}, status=200)

        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=404)        
        
class LogoutAV(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[decode_jwt_token]

    def post(self, request):
        response = Response({"message": "Logged out successfully."}, status=200)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response
        