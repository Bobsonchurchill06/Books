import logging
import json
from traceback import format_exc

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from book.models import Users, Books
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class SignUpView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = Users.objects.create(user_name=data['user_name'], is_active=data['is_active'],
                                        email=data['email'], password=data['password'], joined_date=datetime.now())
            return Response({"message": "User_created"}, status=200)
        except Exception as e:
            message = 'error exception in createuser funtion' + \
                str(format_exc())
            logger.error(message)
            return Response({'error': message}, status=400)


class SignInView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user_name = data.get("user_name")
            password = data.get("password")
            user_obj = Users.objects.filter(
                user_name=user_name, password=password).first()
            if user_obj is None:
                return Response({'error': 'invalid username/password'}, status=400)
            return Response({"message": "successfull"}, status=200)

        except Exception as e:
            message = 'error exception in login funtion ' + str(format_exc())
            logger.error(message)
            return Response({'error': message}, status=400)
        
        
class UserUpdateView(APIView):
    def put(self, request):
        try:
            print("ab")
            data = json.loads(request.body)
            user_name = data.get("user_name")
            email = data.get("email")
            password = data.get("password")
            user_obj = Users.objects.filter(user_name=user_name).update(email=email, password=password)
            print(user_obj)
            if user_obj is 0:
                return Response({'error': 'invalid user'}, status=400)
            return Response({"message": "User updated"}, status=200)            
        except Exception as e:
            message = 'error exception in updateuser function' + str(format_exc())
            logger.error(message)
            return Response({'error': message}, status=400)
    
    
class AddBooksView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user_id = data.get("user_id")
            book_name = data.get("book_name")
            description = data.get("description")
            user_obj = Users.objects.get(id=user_id)
            if user_obj:
                book = Books.objects.create(book_name=data['book_name'], description=data['description'], user=user_obj)
                return Response({"message": "Book_Added"}, status=200)
            else:
                return Response({'error': "User does not exist"}, status=400)                
        except Exception as e:
            message = 'error exception in addbooks function' + str(format_exc())
            logger.error(message)
            return Response({'error': message}, status=400)
            
        
        

