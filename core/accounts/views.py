import json
from django.contrib.auth import get_user_model
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomUserSerializer
from .utils import is_phone_number_correct, user_is_already_not_registered, generate_number, check_password, check_name, check_email

# Create your views here.

class RegisterView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [~IsAuthenticated]

    def generate_otp(self):
        otp = generate_number()
        return otp

    def sending_sms(self, mobile_phone, otp):
        print(f'given otp for {mobile_phone} is {otp}')
        return True
        # apikey = "n6krueczY5KX_5O5qnpH6cmAoemMAsdjFcU_uJW4UUs="
        # pid = "ibe8ahmuqytxpg9"
        # fnum = "3000505"
        # tnum = mobile_phone
        # p1 = "code"
        # v1 = otp

        # sms_url = f'http://ippanel.com:8080/?apikey={apikey}&pid={pid}&fnum={fnum}&tnum={tnum}&p1={p1}&v1={v1}'
        # response = requests.get(sms_url)
        
        # if response.status_code == 201:
        #     return True
        # return False


    def post(self, request):
        json_data = json.loads(request.body)
            
        phone_number = json_data['phone_number']
        password = json_data['password']
        password_confirm = json_data['password_confirm']

        if user_is_already_not_registered(phone_number):
            if is_phone_number_correct(phone_number):
                if password == password_confirm:
                    otp = self.generate_otp()
                    if self.sending_sms(phone_number, otp):

                        cache.set(phone_number, otp, timeout=300)

                        cache.set(phone_number + '_details', {
                            'phone_number': phone_number,
                            'password': password,
                        }, timeout=300) 

                        return Response({'message': 'کد تایید با موفقیت ارسال شد'}, status=200)
                    else:
                        return Response({'message': "اس ام اس ارسال شد"}, status=400)
                else:
                    return Response({'message': "پسورد ها یکسان نیستند"}, status=400)
            else:
                return Response({'message': 'شماره موبایل درست نیست'}, status=400)
        else:
            return Response({'message': 'این کاربر قبلا ثبت نام کرده'}, status=400)


class ValidateOtpView(APIView):
        
    authentication_classes = [TokenAuthentication]
    permission_classes = [~IsAuthenticated]

    def post(self, request):
        json_data = json.loads(request.body)
        phone_number = json_data['phone_number']
        otp = json_data['otp']

        cached_otp = cache.get(phone_number)
        if cached_otp and str(cached_otp) == otp:
            user_details = cache.get(phone_number + '_details')
            if user_details:
                user = get_user_model().objects.create(
                    phonenumber=user_details['phone_number'],
                    is_active=True
                )
                user.set_password(user_details['password'])
                user.save()

                cache.delete(phone_number)
                cache.delete(phone_number + '_details')

                return Response({'message': 'کاربر با موفقیت ثبت نام کرد'}, status=200)
            else:
                return Response({'message': 'مجدد اقدام کنید'}, status=400)
        else:
            return Response({'message': 'کد تایید نامعتبر است'}, status=400)


class ChangeUserData(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        user = request.user
        json_data = json.loads(request.body)
        first_name = json_data['first_name']
        last_name = json_data['last_name']
        email = json_data['email']

        account = get_user_model().objects.get(id=user.id)
        
        if check_name(first_name) and check_name(last_name) and check_email(email):
            account.first_name = first_name
            account.last_name = last_name
            account.email = email
            account.save()
        else:
            return Response({'message' : 'اطلاعات را درست وارد کنید'}, 400)

        serializer = CustomUserSerializer(account, many=False)
        serialized_data = serializer.data

        return Response(serialized_data)


class ChangeUserPassword(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        json_data = json.loads(request.body)
        password = json_data['new_password']
        password_confirm = json_data['new_password_confirm']

        if check_password(password) and password == password_confirm:
            account = get_user_model().objects.get(id=user.id)
            account.set_password(password)
            account.save()
        else:
            return Response({'message' : 'پسورد ضعیف است'}, 400)

        serializer = CustomUserSerializer(account, many=False)
        serialized_data = serializer.data

        return Response(serialized_data)
