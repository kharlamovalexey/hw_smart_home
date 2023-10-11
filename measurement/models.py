from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Название датчика', max_length=100)
    description = models.CharField(verbose_name='Описание датчика', max_length=100, null=True, blank=True)
    class Meta:
        verbose_name ='Датчик'
        verbose_name_plural ='Датчики'



class Measurement(models.Model):
    sensor = models.ForeignKey(to=Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name ='Измерение'
        verbose_name_plural ='Измерения'