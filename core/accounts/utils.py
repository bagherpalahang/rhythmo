from django.contrib.auth import get_user_model
import math, random
import re

def generate_number():
    digits = "0123456789"
    OTP = ""
    for ـ in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP

def is_phone_number_correct(phone_number):
    if len(phone_number) == 11 and phone_number.startswith('09'):
        return True
    return False


def user_is_already_not_registered(phone_number):
    try:
        get_user_model().objects.get(phonenumber=phone_number)
        return False
    except:
        return True
    

def check_password(password):
    val = True
     
    if len(password) < 8 or len(password) > 20:
        val = False
         
    if not any(char.isdigit() for char in password):
        val = False
         
    return val

def check_name(name):
    val = True

    if len(name) < 3:
        val = False

    return val

def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    is_valid = re.match(pattern, email) is not None

    if len(email) < 3:
        is_valid = False

    return is_valid