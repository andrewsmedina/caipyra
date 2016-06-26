from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from dreams.views import dreams, thankyou

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', dreams),
    url(r'^thankyou/$', thankyou),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
