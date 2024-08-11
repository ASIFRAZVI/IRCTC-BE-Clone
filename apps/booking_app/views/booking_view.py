from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from pathlib import os
from apps.authentication_app.models.user_model import CustomUser
from apps.booking_app.models.booking_model import Booking
from apps.booking_app.serializers.booking_serializer import BookingSerializer, BookingGetSerializer
from rest_framework import permissions
from apps.authentication_app.jwt_processor import decode_jwt_token
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from dotenv import load_dotenv
load_dotenv()

# booking view
class BookingAV(APIView):
    authentication_classes=[decode_jwt_token]
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    # throttle_scope = 'contacts' if we want scope level

    def post(self, request):
        # JWT_SECRET=os.getenv("JWT_SECRET")
        # try:
        #     token = decode_jwt_token(request, JWT_SECRET)
        #     user_id = token.get('user_id')
        # except:
        #      return Response({"error": "Cookies not found"}, status=404)
            
        # try:
        #     authenticated_user = CustomUser.objects.filter(id=user_id).first()      
        # except:
        #         return Response({"error": "User not found"}, status=404)
            
        #add user into a req data  
        # data['user'] = authenticated_user.id

        data=request.data
        data['user'] = request.user.id  #this user validated and comming from DRF JWT Decoder
        
        seializer=BookingSerializer(data=data)
        if not seializer.is_valid():
            return Response({"errors":seializer.errors}, status=404)
        
        seializer.save()
        return Response({"ok":"ohoo! Ticket Booked"}, status=201)
    
    def get(self, request, user_id):
        try:
            user_booked_ticket= Booking.objects.filter(user=user_id)
            if not user_booked_ticket.exists():
                return Response({"error": "No bookings found for this user ID"}, status=404)
            
        except:
            return Response({"error":"Error in getting ticket by user Id"}, status=400)
        serializer = BookingGetSerializer(user_booked_ticket, many=True)
        return Response(serializer.data, status=200) 
    

    

        
        
        

    