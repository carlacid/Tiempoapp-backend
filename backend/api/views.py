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
        # comprobar si existe la ciudad en la DB, sino existe se crea
        # city, created = models.City.objects.get_or_create(name=data["city"]["name"])
        # city = checkCity(data)

        # Comprobar si existe el dia en esa ciudad en la DB, sino existe lo crea
        # for item in data["list"]:

        #     fecha = item["dt_txt"].split()

        #     day, created = models.Day.objects.get_or_create(
        #         day=fecha[0],
        #         city=city,
        #         defaults={'update_at': now()}
        #     )
        #     stamp = dt.datetime.fromtimestamp(item["dt"])
        #     # Si han pasado 2 horas actualizar los registros de tiempo
        #     if not day.update_at or (day.update_at.hour - now().hour)>=2:
        #         # Actualizamos los registros de tiempo
        #         records, created = models.WeatherRecord.objects.update_or_create(
        #             datetime=stamp,
        #             day=day,
        #             defaults={
        #                 'temp_max':item["main"]["temp_max"],
        #                 'temp_min':item["main"]["temp_min"],
        #                 'humidity':item["main"]["humidity"],
        #                 'wind':item["wind"]["speed"],
        #                 'description':item["weather"][0]["description"],
        #                 'icon':item["weather"][0]["icon"],}
        #         )
        #         # Actualizamos la fecha de update con la actual
        #         dayupdate, created = models.Day.objects.update_or_create(
        #             day=fecha[0],
        #             city=city,
        #             defaults={'update_at': now()}
        #         )
        #     else:
        #         # comprobar si existe el tiempo en esa hora en la DB, sino existe se crea
        #         record, created = models.WeatherRecord.objects.get_or_create(
        #             datetime=stamp,
        #             day=day,
        #             defaults={
        #                 'temp_max':item["main"]["temp_max"],
        #                 'temp_min':item["main"]["temp_min"],
        #                 'humidity':item["main"]["humidity"],
        #                 'wind':item["wind"]["speed"],
        #                 'description':item["weather"][0]["description"],
        #                 'icon':item["weather"][0]["icon"],}
        #         )
        return HttpResponse(r)
