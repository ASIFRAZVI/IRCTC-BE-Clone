from django.db import models
from django.utils import timezone
from apps.authentication_app.models.user_model import BaseModel, CustomUser
from apps.booking_app.models.train_model import Train

    
class Booking(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="customuser")
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name="trains")
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    seat_number=models.IntegerField()
    journey_date = models.DateField() 
    
    # # overriding save method
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     SeatAllotment.objects.create(booked_seat=self)
      


