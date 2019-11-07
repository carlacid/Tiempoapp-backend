from db import models

class Methods:

    def __init__(self, data):
        self.data = data

    def checkCity(data):
        city, created = models.City.objects.get_or_create(name=data["city"]["name"])
        return city

    def main():
        checkCity(data)
        for item in data["list"]:
            fecha = item["dt_txt"].split()
            checkDay(fecha, city)
            update(day,item)

    def checkDay(fecha, city):
        day, created = models.Day.objects.get_or_create(
            day=fecha[0],
            city=city,
            defaults={'update_at': now()}
        )

    def update(day, item):
        stamp = dt.datetime.fromtimestamp(item["dt"])
        # Si han pasado 2 horas actualizar los registros de tiempo
        if not day.update_at or (day.update_at.hour - now().hour)>=2:
            # Actualizamos los registros de tiempo
            records, created = models.WeatherRecord.objects.update_or_create(
                datetime=stamp,
                day=day,
                defaults={
                    'temp_max':item["main"]["temp_max"],
                    'temp_min':item["main"]["temp_min"],
                    'humidity':item["main"]["humidity"],
                    'wind':item["wind"]["speed"],
                    'description':item["weather"][0]["description"],
                    'icon':item["weather"][0]["icon"],}
            )
            # Actualizamos la fecha de update con la actual
            dayupdate, created = models.Day.objects.update_or_create(
                day=fecha[0],
                city=city,
                defaults={'update_at': now()}
            )
        else:
            # comprobar si existe el tiempo en esa hora en la DB, sino existe se crea
            record, created = models.WeatherRecord.objects.get_or_create(
                datetime=stamp,
                day=day,
                defaults={
                    'temp_max':item["main"]["temp_max"],
                    'temp_min':item["main"]["temp_min"],
                    'humidity':item["main"]["humidity"],
                    'wind':item["wind"]["speed"],
                    'description':item["weather"][0]["description"],
                    'icon':item["weather"][0]["icon"],}
            )