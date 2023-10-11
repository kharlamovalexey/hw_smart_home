from django.urls import path

from .views import SensorView, SensorDetail, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorDetail.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
