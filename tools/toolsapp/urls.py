from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path('hello/',views.show),   
    path('tools/',views.tools, name='tools'),
    path('home/', views.home, name='home'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('userhome/',views.user_homepage,name='userhome'),
    path('shophome/',views.shop_home,name='shophome'),
    path('shoplogin/',views.shop_login,name='shoplogin')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)