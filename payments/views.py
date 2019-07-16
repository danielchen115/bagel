from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Restaurant
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
import stripe

# Create your views here.

class StripeAuthorizeView(APIView):
    def get(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        url = 'https://connect.stripe.com/oauth/authorize'
        params = {
            'response_type': 'code',
            'scope': 'read_write',
            'client_id': settings.STRIPE_CONNECT_CLIENT_ID,
            'redirect_uri': f'http://localhost:8000/users/oauth/callback'
        }
        url = f'{url}?{urllib.parse.urlencode(params)}'
        return redirect(url)
