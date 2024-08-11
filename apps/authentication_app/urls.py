from django.urls import path
from apps.authentication_app.views import Registration, Login, LogoutAV

urlpatterns=[
    path('signup/', Registration.as_view(), name="signupuser" ),
    path('signin/', Login.as_view(), name="Loginuser"),
    path('logout/', LogoutAV.as_view(), name="logout")
]