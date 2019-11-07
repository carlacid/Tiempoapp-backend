import datetime as dt

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils.timezone import now

import json

import requests

from api.services import getapi
from api.methods import Methods
from db import models


# Create your views here.
class MyView(View):

    def get(self, request, *args, **kwargs):
        print(request.GET)
        city = request.GET['city']
        r=getapi(city)
        data = json.loads(r)

        method = Methods(data)
        method.main

        return HttpResponse(r)
