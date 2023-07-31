
from django.contrib import admin
from django.urls import path,include

from django.contrib.auth import views as auth_views #builtin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('apps.users.urls')),
    path('dashboard/',include('apps.dashboard.urls')),


    path('',auth_views.LoginView.as_view(template_name='users/login.html'),name='login_user'),
    path('users/logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
