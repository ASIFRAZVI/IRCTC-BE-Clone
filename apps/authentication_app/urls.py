from django.urls import path
from apps.authentication_app.views import Registration, Login, LogoutAV, RefreshTokenView

urlpatterns=[
    path('signup/', Registration.as_view(), name="signupuser" ),
    path('signin/', Login.as_view(), name="Loginuser"),
    path('refresh-token/', RefreshTokenView.as_view(), name='refresh-token'),
    path('logout/', LogoutAV.as_view(), name="logout")
]