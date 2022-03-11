from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from photoapp.views import register, login_view, logout_view

urlpatterns=[
    # path('', home_view, name = "dashboard"),
    path('homepage', views.homepage, name='homepage'),
    path('search/', views.search_results, name='search_results'),
    path('update_profile/', views.update_profile, name='update_profile' ),
    path('view_profile/<int:id>', views.view_profile, name='view_profile'),
    path('image/(<int:id>/)', views.image, name='image'),
    path('new_image/', views.new_image, name='new_image'),
    path('', register, name = "register"),
    path('login/', login_view, name = "login" ),
    path('logout/', logout_view, name = "logout" ),  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)