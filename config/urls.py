from django.conf.urls import url, include
from django.contrib import admin
from api.api.v1 import urls as ApiUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(ApiUrls))
]
