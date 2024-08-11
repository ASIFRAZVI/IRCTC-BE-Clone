from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime
from django.utils import timezone #always use timezone
import uuid


class BaseModel(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    is_banned=models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract=True

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('please provide email')
        if not username:
            raise ValueError('plese provide email')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        user.save()

        return user


class CustomUser(AbstractBaseUser, BaseModel):
    full_name=models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True , null=False, blank=False)
    password = models.CharField(max_length=128 ,null=False, blank=False) 
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'


    def __str__(self):
        return self.email or self.full_name