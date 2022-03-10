from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from photoapp.views import register, login_view, logout_view

urlpatterns=[
    # path('', home_view, name = "dashboard"),
    path('', views.homepage, name='homepage'),
    path('search/', views.search_results, name='search_results'),
    path('register/', register, name = "register"),
    path('login/', login_view, name = "login" ),
    path('logout/', logout_view, name = "logout" ),  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)