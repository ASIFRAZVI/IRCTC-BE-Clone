from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from apps.booking_app.serializers.train_serializer import TrainGetSerializer
from apps.booking_app.models.booking_model import Train, Booking
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class TrainAV(APIView):
    permission_classes=[permissions.AllowAny]
    throttle_classes = [AnonRateThrottle]
    
    def post(self, request):
        data= request.data
        serializer=TrainGetSerializer(data=data)
        if not serializer.is_valid():
            return Response({"error":serializer.errors}, status=400)
        serializer.save()
        return Response({"ok":"Train Added!"}, status=201)
    
    def get(self, request, pk=None):
        try:
            if pk is None:
                trains = Train.objects.all()
                serializer = TrainGetSerializer(trains, many=True)
                return Response(serializer.data, status=200)
            
            trains=Train.objects.get(pk=pk)
            booked_seats = Booking.objects.filter(train=trains)
            booked_seats_count=booked_seats.count()
            # print(booked_seats.name)
            # print(booked_seats.seat_number)
            total_seats = trains.total_seats
            
            available_seats = total_seats - booked_seats_count
            serializer = TrainGetSerializer(trains)

            data = serializer.data
            data['available_seats'] = available_seats
            return Response(data, status=200)
        except:
            return Response({"error":"faild to get train"}, status=400)
        
    def put(self, request, pk):
        try:
            instance=Train.objects.get(pk=pk)
        except:
            return Response({"error":"faild to get train"}, status=400)
        
        serializer=TrainGetSerializer(instance, data=request.data)
        if not serializer.is_valid():
            return Response({"error":serializer.error}, status=400)
        serializer.save()
        return Response({"ok":"Train Updated!"}, status=201)
    
    def delete(self, request, pk):
        try:
            instance=Train.objects.get(pk=pk)
        except:
            return Response({"error":"faild to get train"}, status=400)
        instance.delete()
        return Response({"ok":"Train Deleted!"}, status=203)