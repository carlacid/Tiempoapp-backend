from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField("Name", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class Day(models.Model):
    day= models.DateTimeField("Dia", blank=False, null=False)
    city=models.ForeignKey(City, models.CASCADE, null=False, blank=False)
    update_at=models.DateTimeField("Updated at", null=True, blank=True)

    def __str__(self):
        return f"{self.city.name} {self.day}"


class WeatherRecord(models.Model):
    datetime = models.DateTimeField("Date time", blank=False, null=False)
    temp_max = models.DecimalField("Temp max", max_digits=5, decimal_places=2, default=0)
    temp_min = models.DecimalField("Temp min", max_digits=5, decimal_places=2, default=0)
    humidity = models.IntegerField("Humidity", default=0)
    wind = models.DecimalField("Wind", max_digits=5, decimal_places=2, default=0)
    description = models.TextField("Description", default="")
    icon = models.CharField("Icon", max_length=20, default="")
    day = models.ForeignKey(Day, models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f"{self.day.city} {self.day.day} {self.datetime}"