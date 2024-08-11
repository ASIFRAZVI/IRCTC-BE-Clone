from rest_framework import serializers
from apps.authentication_app.models.user_model import CustomUser
from apps.booking_app.models.booking_model import Train, Booking


# booking serializer
class BookingSerializer(serializers.ModelSerializer):
    train = serializers.UUIDField()

    class Meta:
        model=Booking
        fields="__all__"

    # def validate_user(self, value):
    #     if not value:
    #         raise serializers.ValidationError("Must be a valid user.")
    #     user=CustomUser.objects.get(id=value)
    #     user_status=user.is_active
    #     if not user_status:
    #         raise serializers.ValidationError("User is not active.")
    #     return user
    

    def validate_train(self, value):
        if not value:
            raise serializers.ValidationError("Must be a valid train.")
        return Train.objects.get(id=value)

    def validate(self, value):
        seat_input=value.get('seat_number')  
        train_name_input = value.get('train')
        input_journey_date=value.get("journey_date")
        input_seat_number=value.get("seat_number")
        input_source=value.get("source")
        input_destination=value.get("destination")
        
        try:
            train = Train.objects.get(train_name=train_name_input)
            total_seats = train.total_seats
            date_from=train.date_from
            date_upto=train.date_upto
            source=train.source
            destination= train.destination
            
            # check the total seats
            if seat_input > total_seats:
                raise serializers.ValidationError("Invalid Seat number")
            pass
            # check the date range
            if input_journey_date < date_from or input_journey_date > date_upto:
                raise serializers.ValidationError("Train not running on this date.")
            pass 
        
           # check the entered source and destination is proper or not
            if (source.lower() != input_source.lower()) or (destination.lower() != input_destination.lower()):
                raise serializers.ValidationError("Train not running on this route the available.")  
            pass  
            
        except Train.DoesNotExist:
            raise serializers.ValidationError("Invalid train ID.")
        
        # Check if the input seat number is already booked
        # booked_seats = Booking.objects.filter(train__train_name=train_name_input)

        is_seat_booked = Booking.objects.filter(train__train_name=train_name_input, seat_number=input_seat_number).exists()
        # print(is_seat_booked)

        if is_seat_booked:
            raise serializers.ValidationError("This seat is already booked by a different passenger. Kindly select a different seat.")
    
        return value
    
#this is special for getting the booked ticket 
class BookingGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"
            