from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.homepage, name='homepage'),
    path('user/add/', views.add_user, name='add_user' ),
    path('login/', views.user_login, name='user_login'),
    path('my/page/', views.user_page, name='user_page'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
