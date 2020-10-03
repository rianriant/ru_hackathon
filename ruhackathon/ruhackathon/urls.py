from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from main.views import (
    IventListView,
    IventCreateView,
    IventDetailView,
)
from users.views import (
    register,
    update,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    #path('tinymce/', include('tinymce.urls')),
    path('', IventListView.as_view(), name='ivent-list'),
    path('create/', IventCreateView.as_view(), name='ivent-create'),
    path('ivent/<int:pk>/', IventDetailView.as_view(), name='ivent-detail'),
    path('user/', include('users.urls')),
    path('update/', update, name='profile-update'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),
]

# The code below maintains handling of static files in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
