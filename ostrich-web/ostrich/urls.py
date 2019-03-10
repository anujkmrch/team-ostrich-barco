# from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: get-light-status-from-qr/y19SVa112kjx
    url(r'^/(?P<qrcode>[\w\-]+)/$', views.getLightStatus, name='detail'),
    # ex: /polls/5/results/
    # path('getVehicleDensity', views.results, name='results'),
]