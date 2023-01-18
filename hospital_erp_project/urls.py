from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from .import views, hod_views, staff_views, doctor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),
    path('', views.login_user, name='login_user'),
    path('dologin/', views.dologin, name='dologin'),
    path('dologout/', views.dologout, name='dologout'),

    # This is HOD Panel URL
    path('hod/home', hod_views.home, name='hod_home'),

    #This is Profile URL
    path('profile/', views.profile, name='profile'),

    # This is Profile Update URL
    path('profile/update', views.profile_update, name='profile_update'),

    #Patient Registration
    path('hod/patient/add', views.patient_add, name='patient_add'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)