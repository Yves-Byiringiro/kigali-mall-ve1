from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from about.views import *
from django.conf.urls.i18n import i18n_patterns 


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('kigalimall/interface/', admin.site.urls),
    path('', include('store.urls')),
    path('user/', include('users.urls')),
    # path('api/', include('api.urls')),



    path('about/', about, name='about'),
    path('contact-us/', contact_us, name='contact_us'),
    path('help/', help, name='help'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-conditions/', terms_conditions, name='terms_conditions'),
    path('i18n/', include('django.conf.urls.i18n')),


]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
