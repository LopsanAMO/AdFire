from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from api.api.v1 import urls as ApiUrls
from api.views import Home, Test

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(ApiUrls)),
    url(r'^$', Home.as_view()),
    url(r'^test/', Test.as_view())
]

urlpatterns += [
    url(
        r'^media/(?P<path>.*)$',
        serve,
        {
            'document_root': settings.MEDIA_ROOT,
        }
    ),
     url(
        r'^static/(?P<path>.*)$',
        serve,
        {
            'document_root': settings.STATIC_ROOT
        }
        )
]
