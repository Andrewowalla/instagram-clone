from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from photoapp.views import register, login_view

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('register/', register, name = "register"),
    path('login/', login_view, name = "login" )
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)