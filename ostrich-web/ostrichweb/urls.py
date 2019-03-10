from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
admin.site.site_header = 'My admin'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^qrcode', include('ostrich.urls'))
]