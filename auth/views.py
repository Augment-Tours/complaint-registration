from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework import serializers
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView
from rest_auth.app_settings import JWTSerializer
from rest_auth.utils import jwt_encode

# Firebase Signup
from firebase_admin import auth

from .enums import STATUS
from .serializers import FirebaseAuthSerializer
from users.models import ShilengaeUser
from users.serializers import ShilengaeUserSignupSerializer

import random
import string

class ConnectToFacebook(generics.GenericAPIView):
    serializer_class = FirebaseAuthSerializer
    permission_classes = [permissions.AllowAny]
    queryset = ShilengaeUser.objects.all()

    def post(self, request, *args, **kwargs):
        validated = auth.verify_id_token(request.data.get('access_token'))

        # check if this facebook id is already linked to an account
        acct_linked = ShilengaeUser.objects.filter(firebase_uid=validated.get('uid')).exists()
        if acct_linked:
            raise serializers.ValidationError('This social account is already linked to a shilengae user')

        user_id = request.data.get('user_id')
        user = get_object_or_404(ShilengaeUser, pk=request.user.pk)
        
        user.firebase_uid = validated.get('uid')
        user.save()

        return Response({'success': True})

class FirebaseLogin(generics.GenericAPIView):
    serializer_class = FirebaseAuthSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        # use access_token to get the access_token from firebase and create a new user if it doesn't exist
        validated = auth.verify_id_token(request.data.get('access_token'))

        user = ShilengaeUser.objects.filter(
            firebase_uid=validated.get('uid')).first()
        if not user:
            password_requirements = string.ascii_uppercase + \
                string.ascii_lowercase + string.digits + '!#$%'
            username_requirements = string.ascii_lowercase + string.digits

            temp_password = random.sample(password_requirements, 10)
            temp_username = random.sample(username_requirements, 15)

            generated_password = "".join(temp_password)
            generated_username = "".join(temp_username)

            data = {
                # TODO: change this country to get fetched either from frontend or from where the request is coming from
                'country': 1,
                # TODO: try to fetch from facebook if auth method is facebook
                'email': '',
                'first_name': validated.get('name').split(' ')[0],
                'last_name': validated.get('name').split(' ')[1],
                'password1': generated_password,
                'password2': generated_password,
                'status': STATUS.ACTIVE,
                'type': ShilengaeUser.ROLE.USER,
                'username': generated_username,
                'firebase_uid': validated.get('uid')
            }

            signup_serializer = ShilengaeUserSignupSerializer(data=data)
            signup_serializer.is_valid()
            signup_serializer.save(request=request)



        user = ShilengaeUser.objects.filter(firebase_uid=validated.get('uid')).first()
        token = jwt_encode(user)

        user_data = {
            'user': user,
            'token': token
        }
        
        return Response(JWTSerializer(user_data).data,
                        status=status.HTTP_201_CREATED)
