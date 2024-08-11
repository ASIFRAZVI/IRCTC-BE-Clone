from django.urls import path
from apps.booking_app.views.booking_view import BookingAV
from apps.booking_app.views.train_view import TrainAV


urlpatterns=[
    path("get-trains/", TrainAV.as_view(), name="get-all-trains"),
    path("get-trains/<str:pk>", TrainAV.as_view(), name="get-all-trains"),

    #booking paths
    path("book-ticket/", BookingAV.as_view(), name="book-ticket"),
    path("book-ticket/<str:user_id>", BookingAV.as_view(), name="book-ticket")
]