from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class CustomUserManager(UserManager):

    def _create_user(self, phonenumber, email, password, **extra_fields):

        if not phonenumber:
            raise ValueError("The given phonenumber must be set")
        
        email = self.normalize_email(email)
        user = self.model(phonenumber=phonenumber, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, phonenumber, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phonenumber, email, password, **extra_fields)

    def create_superuser(self, phonenumber, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phonenumber, email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    phonenumber = PhoneNumberField(unique=True)
    email = models.EmailField(unique=False, blank=True)
    USERNAME_FIELD = "phonenumber"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return str(self.phonenumber)
