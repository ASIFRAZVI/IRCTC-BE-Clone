from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.authentication_app.models.user_model import BaseModel
from apps.authentication_app.models.user_model import CustomUser


class Train(BaseModel):
    train_number = models.CharField(max_length=20, unique=True)
    train_name=models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField(default=timezone.now)
    arrival_time = models.TimeField(default=timezone.now)   
    total_seats = models.PositiveIntegerField()
    date_from = models.DateField()
    date_upto=models.DateField()

    def __str__(self):
        return self.train_name
    
class Review(BaseModel):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="review_user")
    rating=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description= models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user} - {self.rating} - {self.description[:50]}..."