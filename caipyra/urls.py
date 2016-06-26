from django.conf.urls import url
from django.contrib import admin

from dreams.views import dreams

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', dreams),
]
